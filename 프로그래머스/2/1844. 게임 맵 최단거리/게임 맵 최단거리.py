from collections import deque

def solution(maps):
    q = deque()
    q.append((0,0))
    
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    
    n = len(maps)
    m = len(maps[0])
    
    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1
        
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if dist[nx][ny] == 0:
                    q.append((nx,ny))
                    dist[nx][ny] = dist[x][y] + 1

    return dist[n - 1][m - 1] if dist[n - 1][m - 1] != 0 else -1 