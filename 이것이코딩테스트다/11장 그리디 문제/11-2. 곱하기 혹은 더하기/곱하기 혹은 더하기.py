def solution(s):
    init = int(s[0])
    
    for num in s[1:]:
        num = int(num)
        if init <= 1 or num <= 1:
            init += num
        else:
            init *= num
    return init
