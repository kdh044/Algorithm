import sys
input = sys.stdin.readline

n,k = map(int,input().split())

result = 0

while (n >= k):
    target = (n // k) * k
    result += n - target
    
    n //= k
    result += 1
result += n - 1
print(result)
