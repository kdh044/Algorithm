# 문제 제작 가이드 (이것이 코딩 테스트다)

> **채점 인터프리터는 PyPy3** (`judge/pypy/pypy3.exe`, core.PY). ref.py·slow.py·제출 코드 모두 PyPy로 실행·측정됨.
> PyPy에는 numpy 등 외부 패키지가 없음. 반복문은 CPython보다 약 8배 빠르고 시작 시간은 약 80ms.
> 따라서 입력 조건의 **책 최댓값을 그대로** 쓰는 것이 원칙(파일 15MB 이하). 의도된 복잡도의 평범한 풀이(책 저자 코드)는 PyPy에서 통과,
> 한 단계 나쁜 복잡도는 PyPy에서도 TLE 나야 함.

작업 폴더: `C:/Users/danny/Desktop/코테/judge`
- 책 OCR 텍스트: `C:/Users/danny/AppData/Local/Temp/claude/C--Users-danny-Desktop---/936f8f89-4793-4d6a-b9d8-72efaa2b0d03/scratchpad/book.txt` (`=====PAGE n=====` 구분, OCR 오타 많음)
- 저자 정답 코드: `.../scratchpad/ref/<장>/<번호>.py`, 문제-파일 대응표는 `.../scratchpad/ref/README.md`
- 완성 예시: `problems/11-1/` (반드시 먼저 읽을 것)

## 문제 하나 = `problems/<장>-<장 안 순번>/`
장 안 순번은 그 장에서 책에 나오는 순서(1부터). Part2(3~10장)는 "실전 문제"만(이론 예제 제외), Part3(11~19장)는 기출문제 전부.

- `problem.json`
  - `id`, `chapter`(int), `chapterName`(예: "그리디", "그리디 문제"), `title`
  - `type`: `"stdin"`(표준입출력) 또는 `"function"`(프로그래머스식 solution 함수, 카카오 문제 등). function이면 `"func": "solution"`, 그리고 `"signature": "def solution(s):"` 넣기
  - `timeLimit`(초, 책 기준), `memoryLimit`(MB), `difficulty`(책의 난이도 별 개수 "1"~"3", 반 개는 "1.5"·"2.5", 모르면 ""), `solveMinutes`(책의 풀이 시간), `source`(예: "2020 카카오 신입 공채", "핵심 유형"), `link`(책에 있는 백준/프로그래머스 링크, 없으면 "")
  - `checker`: 생략=정확히 일치(줄 끝 공백/마지막 빈 줄 무시), `"tokens"`=공백 무시, `"float"`=실수 오차 1e-6
  - `samples`: 책 예제. stdin형 `[{"input": "...\n", "output": "...\n"}]`, function형 `[{"args": [...], "expected": ...}]`
- `statement.md`: 문제 설명(마크다운). OCR 오타를 바로잡아 **책 문장 그대로** 깔끔하게 복원. 표/격자 예시는 코드블록. `## 입력 조건`, `## 출력 조건` 섹션 포함(function형은 `## 제한 사항`). 예제 입출력은 samples로 자동 표시되니 statement에 쓰지 않음. 그림이 필요한 설명은 글이나 ASCII로 대신.
- `ref.py`: 저자 정답 코드 복사. 너무 느려서 최대 케이스가 시간제한 60%를 넘으면 같은 결과를 내는 더 빠른 코드로 바꿔도 됨(정답 동일성은 slow/brute로 작은 케이스 대조해 확인).
- `gen.py`: `def generate(rng)` -> stdin형 `[{"name","input"}]`, function형 `[{"name","args"}]`. 15~25개 정도:
  - 경계값(최소 크기, 0/1, 전부 같은 값, 정렬/역정렬, 답이 0이나 -1인 경우 등)
  - 작은 랜덤 여러 개
  - **시간복잡도 검증용 최대 크기 케이스 2~4개**: 입력 조건의 최댓값으로. 의도된 복잡도(예: N=10^6이면 O(N log N))는 통과하고, 한 단계 나쁜 풀이(예: O(N^2))는 확실히 시간초과 나도록. 최악 케이스 구조(예: 다익스트라는 간선 최대, 이진탐색은 범위 최대, 그리디 반례 등)를 의식해서 설계.
  - 입력 조건을 절대 위반하지 말 것(문제에 "답이 항상 존재" 같은 보장이 있으면 지키도록 생성).
- `slow.py`: (가능하면 꼭) 정답은 맞지만 복잡도가 한 단계 나쁜 풀이. build가 "어딘가에서 TLE"를 요구함 → 큰 케이스가 제 역할을 하는지 검증됨. 입력 범위가 작아 완전탐색이 의도된 문제(예: 구현/시뮬레이션, N≤8 등)는 slow.py 생략.

## 빌드/검증
`cd C:/Users/danny/Desktop/코테/judge && python tools/build.py <id> [<id>...]`
- [OK]가 나올 때까지 고칠 것. ref가 예제와 다르면 예제 입력/출력을 책에서 다시 확인.
- 생성 케이스가 너무 커서 .in 파일이 15MB를 넘지 않게.
- 다른 폴더(다른 사람 담당 장)는 건드리지 말 것. core.py/build.py 수정 금지(버그가 있으면 보고만).

## 그림 넣기 (책 페이지에서 잘라내기)
- `python tools/page.py preview <페이지>` → `data/preview/p<페이지>.jpg` 생성(5% 격자, 숫자 눈금). Read 도구로 이미지를 보고 그림 영역 좌표(0~1 비율)를 정함.
- `python tools/page.py crop <페이지> <id> <이름> x0 y0 x1 y1` → `problems/<id>/img/<이름>.png` (흰 여백 자동 정리). 결과 PNG도 Read로 열어 잘 잘렸는지 확인.
- statement.md 의 해당 설명 위치에 `![그림 설명](img/<이름>.png)` 로 삽입. 그림 바로 아래 캡션이 필요하면 `*캡션*` 한 줄.
- 대상: 격자/지도/그래프/트리/카드/진행 과정 등 **문제를 이해하는 데 필요한 그림**. 본문 글자, 입력·출력 예시 박스, 장식은 자르지 않음. 그림 대신 넣어 둔 ASCII 표현은 그림이 같은 내용을 보여주면 지워도 됨(입출력 형식 설명용 코드블록은 유지).
- 페이지 미리보기에서 보이는 **난이도(●●○ → "2", ●◐○ → "1.5"), 풀이 시간, 시간/메모리 제한, 기출 출처**가 problem.json과 다르면 바로잡기(시간 제한을 바꾸면 build 다시 실행).
