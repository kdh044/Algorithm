import math

def solution(n, m, coins):
    d = [math.inf] * (m + 1)
    d[0] = 0

    for i in range(n):
        for j in range(coins[i], m + 1):
            d[j] = min(d[j], d[j - coins[i]] + 1)

    if d[m] == math.inf:
        return -1
    return d[m]
