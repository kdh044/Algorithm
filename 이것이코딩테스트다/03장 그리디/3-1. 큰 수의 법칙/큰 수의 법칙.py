import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()
answer = 0
count = 0

for _ in range(m):
    if count == k:
        answer += nums[-2]
        count = 0
    else:
        answer += nums[-1]
        count += 1
print(answer)
