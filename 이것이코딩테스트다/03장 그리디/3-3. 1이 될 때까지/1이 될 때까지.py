import sys
input = sys.stdin.readline

n,k = map(int,input().split())

answer = 0

while (n >= k):
    target = (n // k) * k
    answer += n - target
    n = target
    
    n //= k
    answer += 1
    
answer += n - 1

print(answer)
