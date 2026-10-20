def solution(s):
    answer = int(s[0])

    for c in s[1:]:
        num = int(c)
        if answer <= 1 or num <= 1:
            answer += num
        else:
            answer *= num
    
    return answer
