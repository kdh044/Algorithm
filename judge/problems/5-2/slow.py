# 거리 완화를 수렴할 때까지 격자 전체에 반복 (O((NM) * 경로 길이))
n, m = map(int, input().split())
g = [input() for _ in range(n)]
INF = 10 ** 9
dist = [[INF] * m for _ in range(n)]
dist[0][0] = 1
changed = True
while changed:
    changed = False
    for i in range(n):
        for j in range(m):
            if g[i][j] != '1' or (i == 0 and j == 0):
                continue
            v = dist[i][j]
            if i > 0 and dist[i - 1][j] + 1 < v:
                v = dist[i - 1][j] + 1
            if i < n - 1 and dist[i + 1][j] + 1 < v:
                v = dist[i + 1][j] + 1
            if j > 0 and dist[i][j - 1] + 1 < v:
                v = dist[i][j - 1] + 1
            if j < m - 1 and dist[i][j + 1] + 1 < v:
                v = dist[i][j + 1] + 1
            if v < dist[i][j]:
                dist[i][j] = v
                changed = True
print(dist[n - 1][m - 1])
