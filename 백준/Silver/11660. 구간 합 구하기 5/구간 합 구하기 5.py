import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [[0] * (n + 1)]  # 첫 번째 줄 0 패딩
D = [[0] * (n + 1) for _ in range(n + 1)]  # 누적합 배열

for _ in range(n):
    A_row = [0] + list(map(int, input().split()))  # 0 패딩하고 원본 저장
    A.append(A_row)

# 누적합 배열 만들기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

# 질의 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    print(result)
