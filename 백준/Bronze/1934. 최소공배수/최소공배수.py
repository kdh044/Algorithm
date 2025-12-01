import math
n = int(input())

for _ in range(n):
    x, y = map(int,input().split())
    g = math.gcd(x,y)
    l = x * y // g
    print(l)