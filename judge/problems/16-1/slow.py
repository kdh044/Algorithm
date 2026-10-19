# 메모이제이션 없이 모든 경로를 탐색하는 O(n * 3^m) 풀이
def go(dp, n, m, i, j):
    if j == m - 1:
        return dp[i][j]
    best = 0
    for di in (-1, 0, 1):
        ni = i + di
        if 0 <= ni < n:
            best = max(best, go(dp, n, m, ni, j + 1))
    return dp[i][j] + best


# 입력을 먼저 모두 읽어 둔다(채점기가 입력을 다 넘길 수 있도록)
import sys
data = sys.stdin.read().split()
pos = 0
t = int(data[pos]); pos += 1
for tc in range(t):
    n, m = int(data[pos]), int(data[pos + 1]); pos += 2
    array = list(map(int, data[pos:pos + n * m])); pos += n * m
    dp = [array[i * m:(i + 1) * m] for i in range(n)]
    print(max(go(dp, n, m, i, 0) for i in range(n)))
