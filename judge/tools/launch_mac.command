#!/bin/bash
# 이코테 Judge 실행 (macOS). 처음 실행할 때 PyPy를 자동으로 내려받습니다.
cd "$(dirname "$0")/judge" || exit 1

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3가 없습니다. https://www.python.org/downloads/ 에서 Python 3.11 이상을 설치한 뒤 다시 실행하세요."
  read -r -p "엔터를 누르면 닫힙니다..."
  exit 1
fi
if ! python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)'; then
  echo "Python 3.9 이상이 필요합니다 (현재: $(python3 --version)). https://www.python.org/downloads/ 에서 최신 버전을 설치하세요."
  read -r -p "엔터를 누르면 닫힙니다..."
  exit 1
fi

if [ ! -x pypy/bin/pypy3 ]; then
  V=pypy3.11-v8.0.0
  if [ "$(uname -m)" = "arm64" ]; then A=macos_arm64; else A=macos_x86_64; fi
  echo "채점용 PyPy를 내려받는 중입니다 ($V-$A, 약 30MB)..."
  TMP="$(mktemp -d)"
  if curl -L --fail --progress-bar -o "$TMP/pypy.tar.gz" "https://downloads.python.org/pypy/$V-$A.tar.gz" \
     && tar xzf "$TMP/pypy.tar.gz" -C "$TMP" && rm -rf pypy && mv "$TMP/$V-$A" pypy; then
    xattr -dr com.apple.quarantine pypy 2>/dev/null
    echo "PyPy 설치 완료"
  else
    echo "PyPy를 받지 못했습니다. 인터넷 연결을 확인하세요. (PyPy 없이도 실행은 되지만 백준형 문제가 느리게 채점됩니다)"
  fi
  rm -rf "$TMP"
fi

python3 judge.py
