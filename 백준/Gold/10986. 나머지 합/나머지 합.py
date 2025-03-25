import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

# S 배열은 누적합 배열이며, 크기를 n+1로 설정해야 함.
S = [0] * (n + 1) 

# C는 나머지(0~m-1)의 개수를 세는 배열이므로 크기는 m
C = [0] * m

answer = 0

# 누적합 계산
for i in range(n):
    S[i + 1] = S[i] + A[i]

# 누적합의 나머지 카운트
for i in range(1, n + 1):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

# 같은 나머지를 가진 것 중에서 2개를 뽑는 경우의 수 계산
for i in range(m):
    if C[i] > 1:
        answer += C[i] * (C[i] - 1) // 2

print(answer)
