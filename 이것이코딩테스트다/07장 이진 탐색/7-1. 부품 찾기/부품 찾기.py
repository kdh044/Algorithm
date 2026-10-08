import sys
input = sys.stdin.readline

n = int(input())
array = [0] * 10000001
item = set(input().split())

m = int(input())
order = list(input().split())

for x in order:
    if x in item:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')
