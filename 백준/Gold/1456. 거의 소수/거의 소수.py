import math

low, high = map(int,input().split())
limit = int(math.sqrt(high) + 1)
prime = [True] * (limit + 1)
prime[0] = prime[1] = False

for i in range(2, int(math.sqrt(limit) + 1)):
    if prime[i]:
        for j in range(i * i, limit + 1, i):
            prime[j] = False

count = 0

for i in range(2, limit + 1):
    if prime[i]:
        x = i * i
        while x <= high:
            if x >= low:
                count += 1
            x *= i
            
print(count)