import math

x , y = map(int,input().split())
g = math.gcd(x,y)
print("1"*g)