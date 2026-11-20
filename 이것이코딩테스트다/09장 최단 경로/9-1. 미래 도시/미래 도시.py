import math

def solution(n, m, roads, x, k):
    INF = math.inf
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        graph[i][i] = 0
    
    for a,b in roads:
        graph[a][b] = 1
        graph[b][a] = 1
        
    for mid in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][mid] + graph[mid][b])
                
    distance = graph[1][k] + graph[k][x]
    
    if distance == INF:
        return -1
    
    return distance
