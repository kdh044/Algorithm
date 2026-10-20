def solution(s):
    group_0 = 0
    group_1 = 0

    for i in range(1, len(s)):
        if s[i] != s[i - 1] and s[i - 1] == "0":
            group_0 += 1
        elif s[i] != s[i - 1] and s[i - 1] == "1":
            group_1 += 1
    if s[-1] == "0":
        group_0 += 1
    else:
        group_1 += 1
          
    return min(group_0,group_1)
