from collections import deque

def solution(n, m, k, x, roads):
    
    g = [[] for _ in range(n + 1)]
    dist = [-1] * (n + 1)
    dist[x] = 0
    q = deque()
    q.append(x)
    
    for a,b in roads:
        g[a].append(b)
        
    while q:
        now = q.popleft()
        for next in g[now]:
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                q.append(next)
    answer = []
    
    for i in range(1, n + 1):
        if dist[i] == k:
            answer.append(i)
            
    return answer if answer else [-1]
