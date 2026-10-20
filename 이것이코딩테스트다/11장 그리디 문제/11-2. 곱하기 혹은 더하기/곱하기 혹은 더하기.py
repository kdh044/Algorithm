def solution(s):
    answer = int(s[0])
    
    for num in s[1:]:
        num = int(num)
        if answer <= 1 or num <= 1:
            answer += num
        else:
            answer *= num
    return answer
