import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n,m,start = map(int,input().split())

a = [[]for _ in range(n+1)]

for i in range(m):
    s,e = map(int,input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(n+1):
    a[i].sort()

visited = [False] * (n+1)

def DFS(v):
    print(v,end = ' ')
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            DFS(i)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        print(now_node,end = ' ')
        for i in a[now_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
        
DFS(start)
print()
visited = [False]*(n+1)
BFS(start)