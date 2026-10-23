def solution(n):
    n = str(n)
    mid = len(n) // 2
    
    front = n[:mid]
    back = n[mid:]
    
    int_front = sum(map(int,front))
    int_back = sum(map(int,back))
    
    if int_front == int_back:
        return("LUCKY")
    else:
        return("READY")
