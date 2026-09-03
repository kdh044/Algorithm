from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 51 for _ in range(51)]

    # 직사각형 전체를 1로
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                graph[x][y] = 1

    # 직사각형 내부를 0으로
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                graph[x][y] = 0

    # BFS
    q = deque()
    q.append((characterX, characterY, 0))

    visited = [[False] * 51 for _ in range(51)]
    visited[characterX][characterY] = True

    while q:
        x, y, dist = q.popleft()

        if x == itemX and y == itemY:
            return dist

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx <= 50 and 0 <= ny <= 50:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))