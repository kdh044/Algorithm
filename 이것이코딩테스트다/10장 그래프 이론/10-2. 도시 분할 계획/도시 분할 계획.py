def solution(n, m, roads):
    parent = [i for i in range(n + 1)]
    answer = 0
    
    roads.sort(key=lambda x: x[2])
    
    for a, b , cost in roads:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
            last = cost
            
    return answer - last

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent,a)
    b = find(parent,b)
    
    if a > b:
        parent[b] = a
    else:
        parent[a] = b
