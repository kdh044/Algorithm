# 모든 행성 쌍을 간선으로 보는 완전 그래프 위의 프림 알고리즘: O(N^2)
import sys
data = sys.stdin.buffer.read().split()
n = int(data[0])
xs = list(map(int, data[1::3]))
ys = list(map(int, data[2::3]))
zs = list(map(int, data[3::3]))
INF = float("inf")
dist = [INF] * n
used = [False] * n
dist[0] = 0
result = 0
for _ in range(n):
    u = -1
    best = INF
    for i in range(n):
        if not used[i] and dist[i] < best:
            best = dist[i]
            u = i
    used[u] = True
    result += best
    ux, uy, uz = xs[u], ys[u], zs[u]
    for v in range(n):
        if not used[v]:
            c = min(abs(ux - xs[v]), abs(uy - ys[v]), abs(uz - zs[v]))
            if c < dist[v]:
                dist[v] = c
print(result)
