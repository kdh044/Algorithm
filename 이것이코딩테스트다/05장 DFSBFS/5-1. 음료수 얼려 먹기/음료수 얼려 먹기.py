from collections import deque

def solution(n, m, board):
    answer = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                continue

            answer += 1
            board[i][j] = 1
            q = deque([(i, j)])

            while q:
                x, y = q.popleft()

                if x > 0 and board[x-1][y] == 0:
                    board[x-1][y] = 1
                    q.append((x-1, y))

                if x+1 < n and board[x+1][y] == 0:
                    board[x+1][y] = 1
                    q.append((x+1, y))

                if y > 0 and board[x][y-1] == 0:
                    board[x][y-1] = 1
                    q.append((x, y-1))

                if y+1 < m and board[x][y+1] == 0:
                    board[x][y+1] = 1
                    q.append((x, y+1))

    return answer
