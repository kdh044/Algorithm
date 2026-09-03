from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    N = 51  # 좌표 범위: 1 ~ 50

    # 1. 칸(i, j) = 정사각형 [i,i+1] x [j,j+1] 가 어떤 직사각형에 덮여 있는지 표시
    filled = [[False] * N for _ in range(N)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1, x2):
            for j in range(y1, y2):
                filled[i][j] = True

    def is_filled(i, j):
        return 0 <= i < N and 0 <= j < N and filled[i][j]

    # 2. 점 (x,y)에서 (x+dx, y+dy)로 가는 변이 "테두리"인지 판별
    #    -> 그 변을 사이에 둔 두 칸 중 하나만 채워져 있으면 테두리
    def is_border_edge(x, y, dx, dy):
        if dx == 1:
            return is_filled(x, y) != is_filled(x, y - 1)
        if dx == -1:
            return is_filled(x - 1, y) != is_filled(x - 1, y - 1)
        if dy == 1:
            return is_filled(x, y) != is_filled(x - 1, y)
        if dy == -1:
            return is_filled(x, y - 1) != is_filled(x - 1, y - 1)

    # 3. 점들 사이를 BFS
    dist = [[-1] * N for _ in range(N)]
    dist[characterX][characterY] = 0
    q = deque([(characterX, characterY)])
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1 and is_border_edge(x, y, dx, dy):
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist[itemX][itemY]