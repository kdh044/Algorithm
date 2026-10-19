# 모든 단순 경로를 DFS로 탐색해 최단 거리를 구하는 완전 탐색 -> 지수 시간
import sys
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
x, k = map(int, input().split())
INF = 10 ** 9


def shortest(s, t):
    best = [INF]
    visited = [False] * (n + 1)

    def dfs(v, d):
        if v == t:
            best[0] = min(best[0], d)
            return
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                dfs(w, d + 1)
        visited[v] = False

    dfs(s, 0)
    return best[0]


d = shortest(1, k) + shortest(k, x)
print(-1 if d >= INF else d)
