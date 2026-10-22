from collections import deque

def solution(n, k, board, s, x, y):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    q = deque()
    viruses = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                viruses.append((board[i][j],i,j))
    viruses.sort()
    
    for virus,i,j in viruses:
        q.append((virus,i,j,0))
    
    while q:
        v, i, j ,t = q.popleft()
        
        if t == s:
            break
  
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = v
                    q.append((v,nx,ny,t+1))
                    
    return board[x - 1][y - 1]
