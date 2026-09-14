def solution(arr):
    
    n = len(arr)
    m = len(arr[0])
    
    if n > m:
        for row in arr:
            row.extend([0] * (n - m))
    
    elif m > n:
        for _ in range(m - n):
            arr.append([0] * m)
    
    return arr