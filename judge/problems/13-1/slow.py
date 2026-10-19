# 리스트의 pop(0)을 큐로 쓰는 BFS: 꺼낼 때마다 O(N)이라 최악 O(N^2)
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
distance = [-1] * (n + 1)
distance[x] = 0
q = [x]
while q:
    now = q.pop(0)
    for nxt in graph[now]:
        if distance[nxt] == -1:
            distance[nxt] = distance[now] + 1
            q.append(nxt)
res = [i for i in range(1, n + 1) if distance[i] == k]
print("\n".join(map(str, res)) if res else -1)
