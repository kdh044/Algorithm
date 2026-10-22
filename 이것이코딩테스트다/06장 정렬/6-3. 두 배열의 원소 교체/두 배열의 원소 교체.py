def solution(n, k, a, b):
    a.sort()
    b.sort(reverse = True)
    
    for i in range(k):
        if a[i] < b[i]:
            a[i] = b[i]
            
    return sum(a)
