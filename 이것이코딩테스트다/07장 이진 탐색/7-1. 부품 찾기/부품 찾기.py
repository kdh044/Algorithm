import sys
input = sys.stdin.readline

n = int(input())
item = set(input().split())

m = int(input())
order = list(input().split())

for x in order:
    if x in item:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')
