"""친구에게 줄 배포용 zip 만들기: python tools/package.py [출력경로]

- 개인 데이터(data/: 제출 기록, 작성 중인 코드), 플랫폼별 PyPy, 책 PDF용 도구는 빼고 묶는다.
- config.json 은 GitHub 연동 없이(repo "") 시작하도록 새로 넣는다.
- 실행 파일: Mac .command (실행 권한 포함), Windows .bat
"""
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # judge/
TOOLS = ROOT / "tools"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "이코테Judge.zip"
TOP = "이코테Judge"

SKIP_DIRS = {"pypy", "data", "__pycache__", ".git"}
SKIP_FILES = {"config.json", "page.py", "package.py", "launch_mac.command", "launch_win.bat", "FRIEND_README.md"}


def add_text(z, arc, text, mode=0o644, crlf=False):
    data = text.replace("\r\n", "\n")
    if crlf:
        data = data.replace("\n", "\r\n")
    info = zipfile.ZipInfo(arc, date_time=(2026, 10, 6, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = (0o100000 | mode) << 16
    z.writestr(info, data.encode("utf-8"))


def main():
    n = 0
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in sorted(ROOT.rglob("*")):
            rel = f.relative_to(ROOT)
            if f.is_dir() or any(p in SKIP_DIRS for p in rel.parts) or f.name in SKIP_FILES or f.suffix == ".pyc":
                continue
            z.write(f, f"{TOP}/judge/{rel.as_posix()}")
            n += 1
        add_text(z, f"{TOP}/judge/config.json",
                 json.dumps({"repo": "", "subdir": "이것이코딩테스트다", "push": True, "port": 8000}, ensure_ascii=False, indent=2) + "\n")
        add_text(z, f"{TOP}/이코테 Judge 실행 (Mac).command", (TOOLS / "launch_mac.command").read_text(encoding="utf-8"), 0o755)
        add_text(z, f"{TOP}/이코테 Judge 실행 (Windows).bat", (TOOLS / "launch_win.bat").read_text(encoding="utf-8"), crlf=True)
        add_text(z, f"{TOP}/README.md", (TOOLS / "FRIEND_README.md").read_text(encoding="utf-8"))
    print(f"{OUT}  ({n}개 파일, {OUT.stat().st_size / 1024 / 1024:.0f}MB)")


if __name__ == "__main__":
    main()
