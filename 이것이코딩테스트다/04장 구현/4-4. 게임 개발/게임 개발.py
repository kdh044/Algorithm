import sys
input = sys.stdin.readline

n, m = map(int,input().split())
x, y, direct = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left(direct):
    return (direct - 1) % 4

count = 1
turn_count = 0

while True:
    direct = turn_left(direct)
    nx = x + dx[direct]
    ny = y + dy[direct]
    
    if visited[nx][ny] == 0 and data[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1
    
    if turn_count == 4:
        nx = x - dx[direct]
        ny = y - dy[direct]
        
        if data[nx][ny] == 0:
            x = nx
            y = ny
            turn_count = 0
        else:
            break
print(count)
