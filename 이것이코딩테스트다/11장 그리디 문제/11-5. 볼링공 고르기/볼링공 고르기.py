def solution(n, m, k):
    count = [0] * (m + 1)
    
    for weight in k:
        count[weight] += 1
    
    answer = 0
    remain = n
    
    for i in range(1, m + 1):
        remain -= count[i]
        answer += count[i] * remain
    return answer
