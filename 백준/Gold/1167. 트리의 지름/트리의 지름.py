import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    idx = 1
    while data[idx] != -1:
        graph[node].append((data[idx], data[idx + 1]))
        idx += 2

max_dist = 0
farthest_node = 0
visited = [False] * (V + 1)

def dfs(node, dist):
    global max_dist, farthest_node
    visited[node] = True
    if dist > max_dist:
        max_dist = dist
        farthest_node = node
    for nxt, cost in graph[node]:
        if not visited[nxt]:
            dfs(nxt, dist + cost)

# 1차 DFS
dfs(1, 0)

# 2차 DFS
visited = [False] * (V + 1)
max_dist = 0
dfs(farthest_node, 0)

print(max_dist)
