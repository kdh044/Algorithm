def solution(n):
    n = str(n)
    left = n[:len(n)//2]
    right = n[len(n)//2 :]
    int_left = sum(map(int,left))
    int_right = sum(map(int,right))
    
    if int_left == int_right:
        return "LUCKY"
    else:
        return "READY"
