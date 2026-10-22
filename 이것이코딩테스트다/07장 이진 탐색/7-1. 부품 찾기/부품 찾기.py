def solution(n, parts, m, requests):
    parts = set(parts)
    answer = []
    
    for r in requests:
        if r in parts:
            answer.append("yes")
        else:
            answer.append("no")
            
    return answer
