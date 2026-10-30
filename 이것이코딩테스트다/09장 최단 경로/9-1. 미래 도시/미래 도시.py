from collections import deque

def solution(n, m, roads, x, k):
    graph = [[] for _ in range(n + 1)]

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start, end):
        q = deque([start])
        distance = [-1] * (n + 1)
        distance[start] = 0

        while q:
            now = q.popleft()

            if now == end:
                return distance[now]

            for next_node in graph[now]:
                if distance[next_node] == -1:
                    distance[next_node] = distance[now] + 1
                    q.append(next_node)

        return -1

    dist1 = bfs(1, k)
    dist2 = bfs(k, x)

    if dist1 == -1 or dist2 == -1:
        return -1

    return dist1 + dist2
