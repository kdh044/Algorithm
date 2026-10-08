import sys
input = sys.stdin.readline

n = int(input())
array = [0] * 10000001
for i in input().split():
    array[int(i)] = 1

m = int(input())
order = list(map(int,input().split()))

for x in order:
    if array[x] == 1:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')
