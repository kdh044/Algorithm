from collections import deque
def solution(n, k, apples, l, turns):
    snake = deque([[1,1]])
    time = 0
    dr, dc = 0 , 1
    turns = dict(turns)
        
    while True:
        time += 1
        r,c = snake[-1]
        r , c = dr + r, dc + c
        if not(1 <= r <= n and 1 <= c <= n):
            return time
        if [r , c] in snake:
            return time
        
        snake.append([r,c])
        if [r,c] in apples:
            apples.remove([r,c])
        else:
            snake.popleft()
        
        if time in turns:
            if turns[time] == "D":
                dr,dc = dc ,-dr
            else:
                dr, dc = -dc, dr
    return time
