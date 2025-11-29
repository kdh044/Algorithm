import math
n = int(input())
a = [True] * (2000000)
a[0] = a[1] = False

for i in range(2, int(math.sqrt(2000000)) + 1):
    if a[i]:
        for j in range(i * i, 2000000, i):
            a[j] = False
            
def is_pal(x):
    s = str(x)
    return s == s[::-1]

for num in range(n, 2000000):
    if a[num] and is_pal(num):
        print(num)
        break