import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()

total = 0
acc = 0

for i in a:
    acc += i
    total += acc
print(total)