import math
n = int(input())
a = list(map(int,input().split()))

count = 0
for x in a:
    if x < 2:
        continue
    is_prime = True
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
        
print(count)