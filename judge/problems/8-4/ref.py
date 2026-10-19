# 저자 답안(8-8)과 같은 보텀업 DP. min() 호출을 비교문으로 바꿔 상수만 줄인 버전
import sys
input = sys.stdin.readline

# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = [int(input()) for _ in range(n)]

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)
d[0] = 0
for k in array:
    for j in range(k, m + 1):
        v = d[j - k] + 1
        if v < d[j]:
            d[j] = v

# 계산된 결과 출력
print(-1 if d[m] == 10001 else d[m])
