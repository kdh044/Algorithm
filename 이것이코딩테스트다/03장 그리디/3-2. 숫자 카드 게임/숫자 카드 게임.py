def solution(n, m, cards):
    answer = 0
    
    for row in cards:
        answer = max(answer,min(row))
        
    return answer
