from collections import deque
def solution(n, m, board):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    answer = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                q = deque()
                q.append((i,j))
                board[i][j] = 1
                
                while q:
                    x ,y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < n and 0 <= ny < m:
                            if board[nx][ny] == 0:
                                q.append((nx,ny))
                                board[nx][ny] = 1

                answer += 1
        
    return answer
