def solution(n, fears):
    answer = 0
    count = 0
    
    fears.sort()
    
    for i in range(n):
        count += 1
        if count >= fears[i]:
            answer += 1
            count =0
            
    return answer
