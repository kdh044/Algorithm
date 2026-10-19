# 학생 쌍 (i, j)마다 BFS로 i -> j 또는 j -> i 도달 가능 여부를 따로 확인: O(N^2 * (N + M))
import sys
from collections import deque

data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = int(data[2 + 2 * i]), int(data[3 + 2 * i])
    graph[a].append(b)


def reachable(s, t):
    visited = [False] * (n + 1)
    visited[s] = True
    q = deque([s])
    while q:
        u = q.popleft()
        if u == t:
            return True
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return False


result = 0
for i in range(1, n + 1):
    ok = True
    for j in range(1, n + 1):
        if i != j and not reachable(i, j) and not reachable(j, i):
            ok = False
            break
    if ok:
        result += 1
print(result)
