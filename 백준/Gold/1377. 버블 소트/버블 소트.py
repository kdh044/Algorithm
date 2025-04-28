import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()),i))

A.sort()

Max = 0

for i in range(N):
    if Max < A[i][1] - i:
        Max = A[i][1] - i
        
print(Max + 1)