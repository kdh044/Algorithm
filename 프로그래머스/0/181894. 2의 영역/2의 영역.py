def solution(arr):
    idx = []
    
    if 2 not in arr:
        return [-1]
    for i in range(len(arr)):
        if arr[i] == 2:
            idx.append(i)
    a = idx[0]
    b = idx[-1]
    return arr[a:b + 1]