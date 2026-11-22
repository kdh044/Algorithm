def solution(n, m, operations):
    parent = [i for i in range(n + 1)]
    answer = []
    
    for oper, a, b in operations:
        if oper == 0:
            union(parent,a,b)  
        else:
            if find(parent, a) == find(parent, b):
                answer.append("YES")
            else:
                answer.append("NO")
    return answer 
    
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
    
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
        
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
