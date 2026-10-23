def solution(s):
    answer = []
    for i in range(len(s)):
        c = int(s[i])
        answer.append(c)
    
    real_answer = 0
    for d in answer:
        if d == 0:
            continue
        elif d == 1:
            real_answer += d
        else:
            if real_answer > 1:
                real_answer *= d
                
            elif real_answer == 1:
                real_answer += d
                
            else:
                real_answer = 1
                real_answer *= d
                
    return real_answer
