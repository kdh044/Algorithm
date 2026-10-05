import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()

answer = (nums[-1] * k + nums[-2]) * (m // (k + 1))
answer += nums[-1] * (m % (k + 1))

print(answer)
