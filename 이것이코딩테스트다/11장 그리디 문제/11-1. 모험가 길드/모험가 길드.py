def solution(n, fears):
    fears.sort()
    
    group = 0
    answer = 0
    
    for fear in fears:
        group += 1
        
        if group >= fear:
            answer += 1
            group = 0
    return answer
