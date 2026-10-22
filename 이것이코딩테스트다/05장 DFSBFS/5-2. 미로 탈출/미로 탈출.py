from collections import deque

def solution(n, m, maze):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    
    q = deque()
    q.append((0,0))
        
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if  0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    q.append((nx,ny))
                    
    return maze[n - 1][m - 1]
