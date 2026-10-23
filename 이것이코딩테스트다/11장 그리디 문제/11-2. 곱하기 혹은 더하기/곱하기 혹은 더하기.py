def solution(s):
    answer = 0

    for num in s:
        num = int(num)

        if answer <= 1 or num <= 1:
            answer += num
        else:
            answer *= num

    return answer
