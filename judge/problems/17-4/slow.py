# 우선순위 큐 없이 매번 최솟값을 선형 탐색하는 다익스트라: O(N^2)
import sys
_lines = iter(sys.stdin.read().splitlines())
input = lambda: next(_lines)
INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dist = [INF] * (n + 1)
visited = [False] * (n + 1)
dist[1] = 0
for _ in range(n):
    best = INF + 1
    u = -1
    for i in range(1, n + 1):
        if not visited[i] and dist[i] < best:
            best = dist[i]
            u = i
    if u == -1:
        break
    visited[u] = True
    for v in graph[u]:
        if dist[u] + 1 < dist[v]:
            dist[v] = dist[u] + 1
mx = max(dist[1:])
node = dist.index(mx)
print(node, mx, dist.count(mx))
