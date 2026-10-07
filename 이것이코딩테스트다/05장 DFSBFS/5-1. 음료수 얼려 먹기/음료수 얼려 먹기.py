import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 1
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
               
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append((nx,ny))

answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i,j)
            answer += 1
            
print(answer)
