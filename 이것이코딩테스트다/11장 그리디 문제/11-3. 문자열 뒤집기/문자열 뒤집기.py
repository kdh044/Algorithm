def solution(s):
    
    g0 = 0
    g1 = 0
    
    for i in range(1, len(s)):
        
        if s[i] != s[i - 1]:
            if s[i] == "0":
                g0 += 1
            else:
                g1 += 1
        
    if s[0] == "0":
        g0 += 1
    else:
        g1 += 1
        
    return min(g0,g1)
