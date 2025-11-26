import sys

prices = [int(sys.stdin.readline()) for _ in range(5)]

b = min(prices[0:3])
c = min(prices[3:5])

print(b + c - 50)