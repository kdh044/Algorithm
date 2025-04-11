import sys
input = sys.stdin.readline

a = int(input())
n = [int(input()) for _ in range(a)]
n.sort()

for i in n:
    print(i)