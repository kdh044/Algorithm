def solution(n, moves):
    x,y = 1,1
    
    for move in moves:
        if  y + 1 <= n and move == "R":
            y += 1
        elif 0 < y - 1 and move == "L":
            y -= 1
        elif x + 1 <= n and move == "D":
            x += 1
        elif 0 < x - 1 and move == "U":
            x -= 1
        
    return [x,y]
