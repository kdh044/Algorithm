# 매번 최소 거리 정점을 선형 탐색하는 프림 알고리즘: O(N^2 + M)
import sys
data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
graph = [[] for _ in range(n)]
total = 0
for i in range(m):
    x, y, z = int(data[2 + 3 * i]), int(data[3 + 3 * i]), int(data[4 + 3 * i])
    graph[x].append((y, z))
    graph[y].append((x, z))
    total += z
INF = float("inf")
dist = [INF] * n
used = [False] * n
dist[0] = 0
mst = 0
for _ in range(n):
    u = -1
    best = INF
    for i in range(n):
        if not used[i] and dist[i] < best:
            best = dist[i]
            u = i
    used[u] = True
    mst += best
    for v, z in graph[u]:
        if not used[v] and z < dist[v]:
            dist[v] = z
print(total - mst)
