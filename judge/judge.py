"""이코테 로컬 채점 서버.  실행: python judge.py  ->  http://localhost:8000"""
import json
import re
import subprocess
import sys
import tempfile
import threading
import time
import uuid
import webbrowser
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import core

sys.stdout.reconfigure(encoding="utf-8")

ROOT = core.ROOT
DATA = ROOT / "data"
DRAFTS = DATA / "drafts"
STATUS_FILE = DATA / "status.json"
# 설정: judge/config.json (없으면 기본값)
#   repo   : 풀이를 커밋할 git 저장소 경로 (judge 폴더 기준 상대경로 또는 절대경로). "" 이면 GitHub 연동 안 함
#   subdir : 저장소 안에서 풀이를 넣을 폴더
#   push   : 커밋 후 push 여부
CONFIG = {"repo": "../Algorithm", "subdir": "이것이코딩테스트다", "push": True, "port": 8000}
if (ROOT / "config.json").exists():
    CONFIG.update(json.loads((ROOT / "config.json").read_text(encoding="utf-8")))
REPO = (ROOT / CONFIG["repo"]).resolve() if CONFIG.get("repo") else None
if REPO and not (REPO / ".git").exists():
    REPO = None
REPO_SUBDIR = CONFIG["subdir"]
PORT = int(CONFIG.get("port", 8000))
LOCAL_SOLUTIONS = DATA / "solutions"  # 저장소가 없을 때 풀이 저장 위치

DRAFTS.mkdir(parents=True, exist_ok=True)
status_lock = threading.Lock()
git_lock = threading.Lock()
jobs = {}
git_log = []  # 최근 커밋/푸시 결과


def load_status():
    if STATUS_FILE.exists():
        return json.loads(STATUS_FILE.read_text(encoding="utf-8"))
    return {}


def save_status(st):
    STATUS_FILE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")


def record(pid, verdict, time_ms, passed, total):
    with status_lock:
        st = load_status()
        s = st.setdefault(pid, {"solved": False, "attempts": 0, "history": []})
        s["attempts"] += 1
        if verdict == "AC":
            s["solved"] = True
            s["bestMs"] = min(time_ms, s.get("bestMs", 10**9))
        s["history"].insert(0, {"at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "verdict": verdict,
                                "timeMs": time_ms, "passed": passed, "total": total})
        s["history"] = s["history"][:30]
        save_status(st)


# ---------------- 채점 ----------------

def run_job(job, meta, code, mode):
    tmpdir = Path(tempfile.mkdtemp(prefix="icote_"))
    code_path = tmpdir / "solution.py"
    code_path.write_text(code, encoding="utf-8")
    tests = core.list_tests(meta["dir"], meta)
    if mode == "sample":
        tests = [t for t in tests if t.startswith("s")]
    job["total"] = len(tests)
    results = []
    verdict, worst = "AC", 0
    for t in tests:
        r = core.run_case(meta, code_path, t)
        r["name"] = t
        r["sample"] = t.startswith("s")
        if mode == "submit" and not r["sample"]:
            # 숨겨진 케이스는 입출력을 보여주지 않음 (실제 코테처럼)
            r.pop("got", None)
            r.pop("expected", None)
        results.append(r)
        job["done"] = len(results)
        job["results"] = results
        worst = max(worst, r["time_ms"])
        if r["status"] != "AC":
            verdict = r["status"]
            if mode == "submit":
                break
    job["verdict"] = verdict
    job["timeMs"] = worst
    passed = sum(1 for r in results if r["status"] == "AC")
    if mode == "submit":
        record(meta["id"], verdict, worst, passed, len(tests))
        if verdict == "AC":
            job["git"] = {"state": "pending"}
            threading.Thread(target=commit_solution, args=(job, meta, code, worst, len(tests)), daemon=True).start()
    job["finished"] = True


def run_custom(meta, code, stdin):
    tmpdir = Path(tempfile.mkdtemp(prefix="icote_"))
    code_path = tmpdir / "solution.py"
    code_path.write_text(code, encoding="utf-8")
    start = time.perf_counter()
    try:
        p, _ = core.run_with_file_stdin([core.interpreter(meta)[0], str(core.RUNNER), str(code_path)], stdin, meta["timeLimit"] + 2,
                                        dict(__import__("os").environ, PYTHONIOENCODING="utf-8"), cwd=str(tmpdir))
        return {"stdout": p.stdout[-20000:], "stderr": p.stderr[-5000:], "code": p.returncode,
                "time_ms": int((time.perf_counter() - start) * 1000)}
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": "시간 초과", "code": -1, "time_ms": int((meta["timeLimit"] + 2) * 1000)}


# ---------------- GitHub 커밋 ----------------

def safe(name):
    return re.sub(r'[\\/:*?"<>|]', "", name).strip()


def solution_folder(meta):
    ch = f"{meta['chapter']:02d}장 {meta['chapterName']}"
    base = REPO / REPO_SUBDIR if REPO else LOCAL_SOLUTIONS
    return base / safe(ch) / safe(f"{meta['id']}. {meta['title']}")


def bar(solved, total, title, width=500):
    from urllib.parse import quote
    pct = int(solved / total * 100) if total else 0
    return (f"![{pct}%](https://progress-bar.xyz/{solved}/?scale={total}&title={quote(title)}"
            f"&width={width}&color=babaca&suffix=/{total})")


def write_progress_readme():
    """GitHub의 이것이코딩테스트다/README.md: 전체·장별 진행바와 문제표 (푼 여부는 저장소 폴더 기준)"""
    from urllib.parse import quote
    probs = [m for m in core.list_problems() if m["testCount"]]
    chapters = {}
    for m in probs:
        chapters.setdefault(m["chapter"], []).append(m)
    base = REPO / REPO_SUBDIR if REPO else LOCAL_SOLUTIONS
    solved_all = sum(1 for m in probs if solution_folder(m).exists())
    lines = ["# 이것이 취업을 위한 코딩 테스트다 with 파이썬", "",
             "> 나동빈 저, 한빛미디어 · 로컬 채점기(이코테 Judge)에서 모든 테스트를 통과하면 자동으로 커밋됩니다.", "",
             "## 전체 현황", "", bar(solved_all, len(probs), "progress"), "",
             "| 장 | 진행 |", "| :-- | :-- |"]
    for ch, ms in sorted(chapters.items()):
        name = f"{ch:02d}장 {ms[0]['chapterName']}"
        done = sum(1 for m in ms if solution_folder(m).exists())
        lines.append(f"| [{name}](#{quote(re.sub(r'[^\w\- ]', '', name.lower()).replace(' ', '-'))}) | {bar(done, len(ms), 'progress', 300)} |")
    for ch, ms in sorted(chapters.items()):
        name = f"{ch:02d}장 {ms[0]['chapterName']}"
        done = sum(1 for m in ms if solution_folder(m).exists())
        lines += ["", f"## {name}", "", bar(done, len(ms), "progress"), "",
                  "| 번호 | 문제 제목 | 출처 | 상태 | 정답 코드 |", "| :--: | :-- | :--: | :--: | :--: |"]
        for m in ms:
            f = solution_folder(m)
            title = f"[{m['title']}]({m['link']})" if m.get("link") else m["title"]
            if f.exists():
                code = f.relative_to(base).as_posix() + "/" + safe(m["title"]) + ".py"
                lines.append(f"| {m['id']} | {title} | {m.get('source') or '-'} | ✅ | [정답 코드]({quote(code)}) |")
            else:
                lines.append(f"| {m['id']} | {title} | {m.get('source') or '-'} | | |")
    out = base / "README.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out.relative_to(REPO).as_posix() if REPO else None


def git(*args):
    p = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout + p.stderr).strip()


def stars(difficulty):
    """"1.5" -> "★⯪" (책의 반 개짜리 난이도 표시)"""
    d = float(difficulty or 0)
    return "★" * int(d) + ("⯪" if d % 1 else "") or "-"


def commit_solution(job, meta, code, time_ms, total):
    with git_lock:
        try:
            ch = f"{meta['chapter']:02d}장 {meta['chapterName']}"
            folder = solution_folder(meta)
            folder.mkdir(parents=True, exist_ok=True)
            (folder / f"{safe(meta['title'])}.py").write_text(code.rstrip() + "\n", encoding="utf-8")
            today = datetime.now().strftime("%Y년 %m월 %d일 %H:%M")
            link = f"\n\n[문제 링크]({meta['link']})" if meta.get("link") else ""
            readme = (f"# [이코테 {meta['id']}] {meta['title']}\n\n"
                      f"**{ch}** · 출처: {meta.get('source') or '-'} · 난이도 {stars(meta['difficulty'])}"
                      f"{link}\n\n"
                      f"### 성능 요약\n\n시간: {time_ms} ms, 테스트 {total}/{total} 통과 (시간 제한 {meta['timeLimit']}초)\n\n"
                      f"### 제출 일자\n\n{today}\n\n"
                      f"> 「이것이 취업을 위한 코딩 테스트다 with 파이썬」(나동빈, 한빛미디어) 수록 문제\n")
            (folder / "README.md").write_text(readme, encoding="utf-8")
            readme_rel = write_progress_readme()
            if not REPO:
                job["git"] = {"state": "local", "msg": f"GitHub 저장소가 설정되지 않아 {folder} 에만 저장했습니다. (judge/config.json 의 repo)"}
                return
            rel = folder.relative_to(REPO).as_posix()
            git("add", "--", rel, readme_rel)
            rc, out = git("diff", "--cached", "--quiet")
            if rc == 0:
                job["git"] = {"state": "nochange", "msg": "이전에 커밋한 코드와 같아서 커밋하지 않았습니다."}
                return
            msg = f"[이코테 {meta['id']}] Title: {meta['title']}, Time: {time_ms} ms -IcoteJudge"
            rc, out = git("commit", "-m", msg, "--", rel, readme_rel)
            if rc != 0:
                job["git"] = {"state": "error", "msg": "커밋 실패: " + out[-500:]}
                return
            if not CONFIG.get("push", True):
                job["git"] = {"state": "committed", "msg": "로컬 커밋 완료 (push 꺼짐): " + msg}
                return
            job["git"] = {"state": "pushing", "msg": msg}
            git("pull", "--rebase", "--autostash", "-q")
            rc, out = git("push", "-q", "origin", "HEAD")
            job["git"] = {"state": "pushed" if rc == 0 else "push-error", "msg": msg if rc == 0 else "푸시 실패(커밋은 로컬에 저장됨): " + out[-500:]}
        except Exception as e:  # noqa: BLE001
            job["git"] = {"state": "error", "msg": str(e)}
        finally:
            git_log.insert(0, {"at": datetime.now().strftime("%H:%M:%S"), "id": meta["id"], **job["git"]})
            del git_log[20:]


# ---------------- HTTP ----------------

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send_json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def body(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}")

    def problem(self, pid):
        if not re.fullmatch(r"\d+-\d+", pid) or not (core.PROBLEMS / pid / "problem.json").exists():
            self.send_json({"error": "없는 문제"}, 404)
            return None
        return core.load_problem(pid)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/", "/index.html"):
            body = (ROOT / "static" / "index.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif path == "/api/problems":
            st = load_status()
            out = []
            for m in core.list_problems():
                if not m["testCount"]:
                    continue  # 아직 테스트가 없는(제작 중) 문제는 숨김
                s = st.get(m["id"], {})
                out.append({k: m.get(k) for k in ("id", "chapter", "chapterName", "title", "type", "difficulty",
                                                    "solveMinutes", "source", "testCount")}
                           | {"solved": s.get("solved", False), "attempts": s.get("attempts", 0)})
            self.send_json(out)
        elif path.startswith("/api/problem/"):
            meta = self.problem(path.rsplit("/", 1)[1])
            if not meta:
                return
            d = meta.pop("dir")
            meta["statement"] = (d / "statement.md").read_text(encoding="utf-8")
            draft = DRAFTS / f"{meta['id']}.py"
            meta["draft"] = draft.read_text(encoding="utf-8") if draft.exists() else None
            meta["status"] = load_status().get(meta["id"], {})
            meta["interpreter"] = core.interpreter(meta)[1]
            self.send_json(meta)
        elif path.startswith("/api/job/"):
            job = jobs.get(path.rsplit("/", 1)[1])
            self.send_json(job or {"error": "없음"}, 200 if job else 404)
        elif path.startswith("/asset/"):
            # /asset/<문제ID>/<파일>  -> problems/<ID>/img/<파일>
            from urllib.parse import unquote
            parts = unquote(path).split("/")
            if len(parts) != 4 or not re.fullmatch(r"\d+-\d+", parts[2]) or not re.fullmatch(r"[\w\-. ]+\.(png|jpg|jpeg|gif|svg)", parts[3]):
                self.send_json({"error": "bad path"}, 400)
                return
            f = core.PROBLEMS / parts[2] / "img" / parts[3]
            if not f.is_file():
                self.send_json({"error": "not found"}, 404)
                return
            body = f.read_bytes()
            ctype = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "gif": "image/gif", "svg": "image/svg+xml"}[f.suffix[1:].lower()]
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "max-age=300")
            self.end_headers()
            self.wfile.write(body)
        elif path == "/api/git":
            self.send_json(git_log)
        else:
            self.send_json({"error": "not found"}, 404)

    def do_POST(self):
        path = self.path.split("?")[0]
        if path.startswith("/api/draft/"):
            meta = self.problem(path.rsplit("/", 1)[1])
            if meta:
                (DRAFTS / f"{meta['id']}.py").write_text(self.body().get("code", ""), encoding="utf-8")
                self.send_json({"ok": True})
        elif path.startswith("/api/run/"):
            meta = self.problem(path.rsplit("/", 1)[1])
            if not meta:
                return
            b = self.body()
            mode = b.get("mode", "sample")
            if mode == "custom":
                self.send_json(run_custom(meta, b.get("code", ""), b.get("input", "")))
                return
            jid = uuid.uuid4().hex[:12]
            jobs[jid] = {"id": jid, "mode": mode, "done": 0, "total": 0, "results": [], "finished": False}
            threading.Thread(target=run_job, args=(jobs[jid], meta, b.get("code", ""), mode), daemon=True).start()
            self.send_json({"job": jid})
        else:
            self.send_json({"error": "not found"}, 404)


if __name__ == "__main__":
    url = f"http://localhost:{PORT}"
    # Windows에서는 재사용 옵션이 켜져 있으면 같은 포트에 서버가 여러 개 떠버리므로 끈다
    ThreadingHTTPServer.allow_reuse_address = False
    try:
        srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    except OSError:
        print(f"이미 채점 서버가 실행 중입니다. 브라우저에서 {url} 을 엽니다.")
        webbrowser.open(url)
        sys.exit(0)
    print(f"이코테 채점 서버 실행 중: {url}  (종료: Ctrl+C)")
    if "--no-browser" not in sys.argv:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
