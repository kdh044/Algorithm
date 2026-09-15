import math

def solution(progresses, speeds):
    days = []
    for progress, speed in zip(progresses,speeds):
        days.append(math.ceil((100-progress)/speed))
    
    answer = []
    current = days[0]
    stack = 1
    for day in days[1:]:
        if day <= current:
            stack += 1
        else:
            answer.append(stack)
            stack, current = 1 , day     
                    
    answer.append(stack)
    return answer