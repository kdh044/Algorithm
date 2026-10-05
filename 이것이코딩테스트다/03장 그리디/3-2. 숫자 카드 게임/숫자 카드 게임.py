import sys
input = sys.stdin.readline
n,m = map(int,input().split())

answer = 0
for i in range(n):
    data = list(map(int,input().split()))
    if answer < min(data):
        answer = min(data)
print(answer)
