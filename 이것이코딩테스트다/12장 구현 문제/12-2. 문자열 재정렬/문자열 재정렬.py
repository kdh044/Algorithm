def solution(s):
    total = 0
    letters = []
    has_digit = False
    
    for c in s:
        if c in "0123456789":
            total += int(c)
            has_digit = True
        else:
            letters.append(c)
    
    letters.sort()
    
    if has_digit:
        letters.append(str(total))
        
    return "".join(letters)
