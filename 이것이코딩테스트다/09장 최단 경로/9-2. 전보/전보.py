import heapq
import math
def solution(n, m, c, routes):
    graph = [[] for _ in range(n + 1)]
    distance = [math.inf] * (n + 1)
    
    for x,y,z in routes:
        graph[x].append((y,z))
    
    distance[c] = 0
    
    q = []
    heapq.heappush(q,(0,c))
    
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
            
        for next_node, cost in graph[now]:
            new_dist = dist + cost
            
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q,(new_dist,next_node))
                
    count = -1
    max_distance = 0
    for d in distance:
        if d != math.inf:
            count += 1
            max_distance = max(max_distance,d)
    return(count,max_distance)
