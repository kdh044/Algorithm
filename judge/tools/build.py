"""문제 테스트케이스 생성 및 검증.

사용법: python tools/build.py <문제ID> [<문제ID> ...]   (또는 --all)

문제 폴더 구성:
  problem.json  메타데이터 (samples 포함)
  statement.md  문제 설명
  ref.py        정답 코드 (stdin형: 표준입출력 / function형: solution 함수)
  gen.py        def generate(rng) -> list  (stdin형: [{"name","input"}], function형: [{"name","args"}])
  slow.py       (선택) 시간복잡도가 나쁜 풀이. 큰 케이스에서 반드시 시간초과가 나야 함

검증 항목:
  1. ref.py가 책의 예제 출력과 일치
  2. ref.py가 모든 케이스에서 시간제한의 60% 이내
  3. slow.py가 있으면 적어도 하나의 케이스에서 TLE
"""
import json
import random
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import core  # noqa: E402

REF_RATIO = 0.6
sys.stdout.reconfigure(encoding="utf-8")


def build(pid):
    meta = core.load_problem(pid)
    if meta.get("interfaceVersion") == 2:
        print(f"{pid}: 함수형으로 변환된 기존 테스트를 유지합니다. 원본 생성기/참고 코드는 표준입출력형이며 data/before_programmers.zip에 보관되어 있습니다.")
        return
    d = meta["dir"]
    tdir = d / "tests"
    if tdir.exists():
        shutil.rmtree(tdir)
    tdir.mkdir()
    fn = meta["type"] == "function"

    # 1) 예제
    cases = []
    for i, s in enumerate(meta.get("samples", []), 1):
        name = f"s{i:02d}"
        if fn:
            (tdir / f"{name}.json").write_text(json.dumps({"args": s["args"], "expected": s["expected"]}, ensure_ascii=False), encoding="utf-8")
        else:
            (tdir / f"{name}.in").write_text(s["input"], encoding="utf-8")
            (tdir / f"{name}.out").write_text(s["output"], encoding="utf-8")
        cases.append(name)

    # 2) 생성 케이스: 정답 코드로 기대 출력 계산
    ns = {}
    exec(compile((d / "gen.py").read_text(encoding="utf-8"), "gen.py", "exec"), ns)
    gens = ns["generate"](random.Random(int(meta.get("seed", 20201005))))
    errors = []
    big_tl = max(meta["timeLimit"] * 5, 30)
    for i, g in enumerate(gens, 1):
        name = f"t{i:02d}"
        if fn:
            (tdir / f"{name}.json").write_text(json.dumps({"args": g["args"], "expected": None}, ensure_ascii=False), encoding="utf-8")
        else:
            (tdir / f"{name}.in").write_text(g["input"], encoding="utf-8")
            (tdir / f"{name}.out").write_text("", encoding="utf-8")
        cases.append(name)

    # 생성 케이스의 정답 채우기 (ref 실행 결과를 그대로 기대값으로)
    import subprocess, os  # noqa: E401
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    for name in cases:
        if not name.startswith("t"):
            continue
        if fn:
            case = json.loads((tdir / f"{name}.json").read_text(encoding="utf-8"))
            tmp = tdir / f"_{name}.case"
            tmp.write_text(json.dumps({"func": meta.get("func", "solution"), "args": case["args"]}), encoding="utf-8")
            p = subprocess.run([core.interpreter(meta)[0], str(core.HARNESS), str(d / "ref.py"), str(tmp)], capture_output=True, text=True, encoding="utf-8", env=env, timeout=big_tl)
            tmp.unlink()
            if p.returncode != 0:
                errors.append(f"{name}: ref 실행 오류\n{p.stderr[-800:]}")
                continue
            case["expected"] = json.loads(p.stdout.strip().splitlines()[-1])["result"]
            (tdir / f"{name}.json").write_text(json.dumps(case, ensure_ascii=False), encoding="utf-8")
        else:
            inp = (tdir / f"{name}.in").read_text(encoding="utf-8")
            p = subprocess.run([core.interpreter(meta)[0], str(core.RUNNER), str(d / "ref.py")], input=inp, capture_output=True, text=True, encoding="utf-8", env=env, timeout=big_tl)
            if p.returncode != 0:
                errors.append(f"{name}: ref 실행 오류\n{p.stderr[-800:]}")
                continue
            (tdir / f"{name}.out").write_text(p.stdout, encoding="utf-8")

    # 3) 검증: ref가 전부 AC + 시간 여유
    tl = meta["timeLimit"]
    with ThreadPoolExecutor(2) as ex:
        ref_results = list(ex.map(lambda n: (n, core.run_case(meta, d / "ref.py", n, time_limit=big_tl)), cases))
    worst = 0
    for name, r in ref_results:
        worst = max(worst, r["time_ms"])
        if r["status"] != "AC":
            errors.append(f"{name}: ref 결과 {r['status']}\n  got={r.get('got','')[:200]!r}\n  exp={r.get('expected','')[:200]!r}\n  {r.get('stderr','')[-500:]}")
        elif r["time_ms"] > tl * 1000 * REF_RATIO:
            errors.append(f"{name}: ref가 너무 느림 {r['time_ms']}ms (제한 {tl}s의 {int(REF_RATIO*100)}% 초과)")

    # 4) slow.py는 반드시 어딘가에서 TLE
    slow_info = ""
    if (d / "slow.py").exists():
        with ThreadPoolExecutor(2) as ex:
            sr = list(ex.map(lambda n: (n, core.run_case(meta, d / "slow.py", n)), cases))
        tles = [n for n, r in sr if r["status"] == "TLE"]
        wrong = [n for n, r in sr if r["status"] in ("WA", "RE")]
        if wrong:
            errors.append(f"slow.py가 틀린 답을 냄(시간 말고 정답은 맞아야 함): {wrong}")
        if not tles:
            errors.append("slow.py가 TLE 없이 통과함 -> 큰 케이스가 부족함")
        slow_info = f", slow TLE {len(tles)}/{len(cases)}"

    status = "OK " if not errors else "FAIL"
    print(f"[{status}] {pid} {meta['title']}: 케이스 {len(cases)}개, ref 최대 {worst}ms / 제한 {tl}s{slow_info}")
    for e in errors:
        print("   - " + e.replace("\n", "\n     "))
    return not errors


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--all"]:
        args = [m["id"] for m in core.list_problems()]
    ok = all([build(a) for a in args])
    sys.exit(0 if ok else 1)
