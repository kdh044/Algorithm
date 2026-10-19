@echo off
chcp 65001 >nul
cd /d "%~dp0judge"
where python >nul 2>nul
if errorlevel 1 (
  echo Python이 없습니다. https://www.python.org/downloads/ 에서 Python 3.11 이상을 설치하세요. 설치할 때 "Add python.exe to PATH"를 꼭 체크하세요.
  pause
  exit /b 1
)
if not exist pypy\pypy3.exe (
  echo 채점용 PyPy를 내려받는 중입니다 ^(약 30MB^)...
  powershell -NoProfile -Command "$ProgressPreference='SilentlyContinue'; Invoke-WebRequest https://downloads.python.org/pypy/pypy3.11-v8.0.0-win64.zip -OutFile pypy.zip; Expand-Archive pypy.zip -DestinationPath . -Force; Remove-Item pypy.zip; Rename-Item pypy3.11-v8.0.0-win64 pypy"
)
python judge.py
pause
