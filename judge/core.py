"""채점 코어: 문제 로드, 테스트 실행, 결과 비교."""
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROBLEMS = ROOT / "problems"
HARNESS = ROOT / "harness.py"
RUNNER = ROOT / "runner.py"
# 채점 인터프리터: 실제 시험 환경에 맞춘다.
#   표준입출력 문제(백준·삼성형) -> PyPy3,  solution 함수 문제(카카오·프로그래머스형) -> CPython
def _find_pypy():
    import shutil
    for c in (ROOT / "pypy" / "pypy3.exe", ROOT / "pypy" / "bin" / "pypy3"):  # Windows zip / macOS·Linux tar
        if c.exists():
            return str(c)
    return shutil.which("pypy3")


_PYPY = _find_pypy()
PY = _PYPY or sys.executable
PY_NAME = "PyPy3" if _PYPY else "Python 3 (PyPy 없음)"
CPY = sys.executable
CPY_NAME = "Python " + ".".join(map(str, sys.version_info[:2]))


def interpreter(meta):
    """(실행 파일, 표시 이름)"""
    if meta.get("type") == "function":
        return CPY, CPY_NAME
    return PY, PY_NAME


def load_problem(pid):
    d = PROBLEMS / pid
    meta = json.loads((d / "problem.json").read_text(encoding="utf-8"))
    meta["dir"] = d
    return meta


def list_problems():
    out = []
    for d in PROBLEMS.iterdir():
        f = d / "problem.json"
        if f.exists():
            m = json.loads(f.read_text(encoding="utf-8"))
            m["testCount"] = len(list_tests(d, m))
            out.append(m)

    def key(m):
        c, n = m["id"].split("-")
        return (int(c), int(n))

    return sorted(out, key=key)


def list_tests(d, meta):
    t = Path(d) / "tests"
    if not t.exists():
        return []
    ext = ".json" if meta["type"] == "function" else ".in"
    return sorted(p.stem for p in t.iterdir() if p.suffix == ext)


def normalize_text(s):
    lines = [ln.rstrip() for ln in s.replace("\r\n", "\n").split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def _tokens_equal(a, b, eps):
    ta, tb = a.split(), b.split()
    if len(ta) != len(tb):
        return False
    for x, y in zip(ta, tb):
        if x == y:
            continue
        try:
            if abs(float(x) - float(y)) > eps * max(1.0, abs(float(y))):
                return False
        except ValueError:
            return False
    return True


def compare(meta, got, expected):
    checker = meta.get("checker", "exact")
    if meta["type"] == "function":
        if checker == "float":
            return _tokens_equal(json.dumps(got), json.dumps(expected), 1e-6)
        return got == expected
    g, e = normalize_text(got), normalize_text(expected)
    if checker == "float":
        return _tokens_equal(g, e, 1e-6)
    if checker == "tokens":
        return g.split() == e.split()
    return g == e


def run_with_file_stdin(cmd, stdin_data, timeout, env, cwd=None):
    """입력을 파일로 넘겨 실행. (파이프로 쓰면 입력을 덜 읽은 채 계산하는 코드에서 Windows가 멈춤)"""
    with tempfile.TemporaryFile("w+b") as fin:
        fin.write(stdin_data.encode("utf-8"))
        fin.seek(0)
        start = time.perf_counter()
        p = subprocess.run(cmd, stdin=fin, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=timeout, env=env, cwd=cwd or tempfile.gettempdir())
        return p, time.perf_counter() - start


def run_case(meta, code_path, test_name, time_limit=None):
    """한 케이스 실행 -> dict(status, time_ms, got, expected, stderr)"""
    d = Path(meta["dir"]) / "tests"
    tl = time_limit if time_limit is not None else meta["timeLimit"]
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    if meta["type"] == "function":
        case = json.loads((d / f"{test_name}.json").read_text(encoding="utf-8"))
        expected = case["expected"]
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tf:
            json.dump({"func": meta.get("func", "solution"), "args": case["args"]}, tf)
            case_file = tf.name
        cmd = [interpreter(meta)[0], str(HARNESS), str(code_path), case_file]
        stdin_data = ""
    else:
        stdin_data = (d / f"{test_name}.in").read_text(encoding="utf-8")
        expected = (d / f"{test_name}.out").read_text(encoding="utf-8")
        cmd = [interpreter(meta)[0], str(RUNNER), str(code_path)]
        case_file = None
    try:
        p, elapsed = run_with_file_stdin(cmd, stdin_data, tl + 1.0, env)
    except subprocess.TimeoutExpired:
        return {"status": "TLE", "time_ms": int((tl + 1.0) * 1000), "expected": _short(expected)}
    finally:
        if case_file:
            os.unlink(case_file)
    res = {"time_ms": int(elapsed * 1000), "stderr": p.stderr[-2000:], "expected": _short(expected)}
    if elapsed > tl:
        res["status"] = "TLE"
        return res
    if p.returncode != 0:
        res["status"] = "RE"
        return res
    if meta["type"] == "function":
        try:
            got = json.loads(p.stdout.strip().splitlines()[-1])["result"]
        except Exception:
            res["status"] = "RE"
            res["stderr"] = (res["stderr"] + "\n반환값을 해석할 수 없습니다.").strip()
            return res
        res["got"] = _short(got)
        res["status"] = "AC" if compare(meta, got, expected) else "WA"
    else:
        res["got"] = _short(p.stdout)
        res["status"] = "AC" if compare(meta, p.stdout, expected) else "WA"
    return res


def _short(v, n=3000):
    s = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
    return s if len(s) <= n else s[:n] + f"\n... ({len(s) - n}자 생략)"
