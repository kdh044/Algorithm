import sys
input = sys.stdin.readline

n = int(input())
item = set(map(int,input().split()))

m = int(input())
order = list(map(int,input().split()))

for x in order:
    if x in item:
        print("yes", end=" ")
    else:
        print("no", end=" ")
