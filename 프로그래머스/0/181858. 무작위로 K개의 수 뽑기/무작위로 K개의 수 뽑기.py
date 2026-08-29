def solution(arr, k):
    answer = []
    
    for x in arr:
        if x not in answer:
            answer.append(x)
        
        if len(answer) == k:
            break
    
    while len(answer) < k:
        answer.append(-1)
    return answer