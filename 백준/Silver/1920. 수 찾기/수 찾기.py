import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

a.sort()

for x in b:
    idx = bisect.bisect_left(a, x)
    if idx < n and a[idx] == x:
        print(1)
    else:
        print(0)