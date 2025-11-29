import math

low, high = map(int, input().split())

limit = int(math.sqrt(high)) + 1
prime = [True] * (limit + 1)
prime[0] = prime[1] = False

# 에라토스테네스
for i in range(2, int(limit**0.5)+1):
    if prime[i]:
        for j in range(i*i, limit+1, i):
            prime[j] = False

count = 0
for p in range(2, limit+1):
    if prime[p]:
        x = p * p
        while x <= high:
            if x >= low:
                count += 1
            x *= p

print(count)
