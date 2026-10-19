# 우선순위 큐 없이 매번 최솟값을 선형 탐색하는 다익스트라: O(V^2), V = N^2
import sys
_lines = iter(sys.stdin.read().splitlines())
input = lambda: next(_lines)
INF = int(1e9)
for tc in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    V = n * n
    cost = [graph[i // n][i % n] for i in range(V)]
    dist = [INF] * V
    visited = [False] * V
    dist[0] = cost[0]
    for _ in range(V):
        best = INF + 1
        u = -1
        for i in range(V):
            if not visited[i] and dist[i] < best:
                best = dist[i]
                u = i
        visited[u] = True
        x, y = divmod(u, n)
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < n and 0 <= ny < n:
                v = nx * n + ny
                if dist[u] + cost[v] < dist[v]:
                    dist[v] = dist[u] + cost[v]
    print(dist[V - 1])
