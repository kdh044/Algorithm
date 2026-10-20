def solution(n, fears):
    fears.sort()
    
    group = 0
    answer = 0
    
    for fear in fears:
        group += 1
        
        if group >= fear:
            group = 0
            answer += 1
            
    return answer
