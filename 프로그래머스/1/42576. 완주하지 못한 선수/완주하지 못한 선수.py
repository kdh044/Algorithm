def solution(participant, completion):
    answer = {}
    
    for name in participant:
        answer[name] = answer.get(name,0) + 1
    
    for name in completion:
        answer[name] -= 1
    
    for name in participant:
        if answer[name] >= 1:
            return name