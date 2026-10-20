from collections import deque

def solution(n, m, k, x, roads):
    graph = [[] for _ in range(n + 1)]
    
    for a,b in roads:
        graph[a].append(b)
    
    dist = [-1] * (n + 1)
    dist[x] = 0
    q = deque([x])
    
    while q:
        now = q.popleft()
        
        for nxt in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)
    
    answer = []
    
    for i in range(1, n + 1):
        if dist[i] == k:
            answer.append(i)
            
    return answer if answer else [-1]
