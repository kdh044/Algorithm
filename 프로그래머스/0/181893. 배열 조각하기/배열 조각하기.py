def solution(arr, query):
    for i in range(len(query)):
        a = query[i]
        if i % 2 == 0:
            arr = arr[:a+1]
        else: 
            arr = arr[a:]
    return arr