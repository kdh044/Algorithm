def solution(s):
    s = sorted(s)
     
    letter = ''
    digit = ''
    for c in s:
        if c.isdigit():
            digit += c
        else:
            letter += c
    
    if digit:
        digit = sum(map(int,digit))
        digit = str(digit)
    
    return letter + digit
