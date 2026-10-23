def solution(n, fears):
    fears.sort()
    answer = 0
    count = 0
    
    for i in range(n):
        count += 1
        if count >= fears[i]:
            answer += 1
            count = 0
    
    return answer
