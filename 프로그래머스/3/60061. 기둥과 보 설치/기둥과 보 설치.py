def solution(n, build_frame):
    answer = set()
    
    for x,y,a,b, in build_frame:
        if b == 1:
            answer.add((x,y,a))
            
            if not check(answer):
                answer.remove((x,y,a))
        else:
            answer.remove((x,y,a))
            
            if not check(answer):
                answer.add((x,y,a))

    return [list(i) for i in sorted(answer)]
       
def check(answer):
    for x, y, a in answer:
        if a == 0:
            if y == 0 or (x, y - 1, 0) in answer or (x - 1, y, 1) in answer or (x, y, 1) in answer:
                continue
            else:
                return False
        
        else:
            if (x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer or ((x - 1 , y , 1) in answer and (x + 1, y , 1) in answer):
                continue
            else:
                return False
            
    return True
