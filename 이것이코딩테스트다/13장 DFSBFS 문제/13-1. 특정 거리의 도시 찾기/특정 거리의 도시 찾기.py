from collections import deque

def solution(n, m, k, x, roads):
    graph = [[] for _ in range(n + 1)]
    dist = [-1] * (n + 1)
    dist[x] = 0
    q = deque([x]) 
    
    for a,b in roads:
        graph[a].append(b)
        
    while q:
        now = q.popleft()
        for next in graph[now]:
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                q.append(next)
    answer = []
    
    for i in range(1, n + 1):
        if dist[i] == k:
            answer.append(i)
        
    return answer if answer else [-1]
