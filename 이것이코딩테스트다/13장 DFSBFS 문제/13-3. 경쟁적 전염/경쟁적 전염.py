from collections import deque

def solution(n, k, board, s, x, y):
    viruses = []

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    # 1. 바이러스 위치 저장
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                viruses.append((board[i][j], i, j))

    # 2. 바이러스 번호순 정렬
    viruses.sort()

    # 3. BFS 큐 초기화
    q = deque()

    for virus, i, j in viruses:
        q.append((virus, i, j, 0))

    # 4. BFS로 바이러스 확산
    while q:
        virus,cx, cy , t = q.popleft()

        if t == s:
            break

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = virus
                    q.append((virus,nx,ny,t + 1))

    # 5. S초 후 해당 위치의 바이러스 번호
    return board[x - 1][y - 1]
