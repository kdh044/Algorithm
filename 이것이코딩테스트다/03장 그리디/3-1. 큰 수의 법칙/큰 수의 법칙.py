import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()
first = nums[-1]
second = nums[-2]

answer = 0
count = 0

for _ in range(m):
    if count == k:
        answer += second
        count = 0
    else:
        answer += first
        count += 1

print(answer)
