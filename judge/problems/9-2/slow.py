# 우선순위 큐 없이 매번 최단 거리가 가장 짧은 노드를 선형 탐색하는 다익스트라 O(N^2)
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
distance = [INF] * (n + 1)
visited = [False] * (n + 1)
distance[start] = 0
for _ in range(n):
    now, best = -1, INF
    for i in range(1, n + 1):
        if not visited[i] and distance[i] < best:
            best, now = distance[i], i
    if now == -1:
        break
    visited[now] = True
    for y, z in graph[now]:
        if best + z < distance[y]:
            distance[y] = best + z
count = sum(1 for d in distance[1:] if d != INF)
print(count - 1, max(d for d in distance[1:] if d != INF))
