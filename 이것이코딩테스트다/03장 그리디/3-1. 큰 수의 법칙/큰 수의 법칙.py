def solution(n, m, k, numbers):
    numbers.sort(reverse = True)
    answer = 0
    count = 0
    
    for _ in range(m):
        if count < k:
            answer += numbers[0]
            count += 1
        else:
            answer += numbers[1]
            count = 0
            
    return answer
