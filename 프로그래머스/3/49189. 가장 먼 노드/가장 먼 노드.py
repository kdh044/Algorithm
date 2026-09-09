from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]    
    
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    distance = [-1] * (n + 1) # 방문하지 않는 배열
    distance[1] = 0 # 1번에서 출발하니깐... 0으로 둠
    
    q = deque([1]) # 1에서 출발
    
    while q:
        s = q.popleft()
        
        for e in graph[s]:
            if distance[e] == -1:
                distance[e] = distance[s] + 1
                q.append(e)
        
    return distance.count(max(distance))