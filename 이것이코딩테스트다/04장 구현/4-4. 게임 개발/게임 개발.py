def solution(n, m, a, b, d, board):
    visited = [[0] * m for _ in range(n)]
    visited[a][b] = 1

    dx = [-1, 0, 1, 0]  
    dy = [0, 1, 0, -1]

    answer = 1
    turn = 0

    while True:
        d = (d - 1) % 4

        nx = a + dx[d]
        ny = b + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0 and visited[nx][ny] == 0:
                a, b = nx, ny
                visited[a][b] = 1
                answer += 1
                turn = 0
                continue

        turn += 1

        if turn == 4:
            nx = a - dx[d]
            ny = b - dy[d]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                a, b = nx, ny
                turn = 0
            else:
                break

    return answer
