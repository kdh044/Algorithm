# 저자 풀이(플로이드 워셜)와 같은 도달 가능성 판정을 비트셋으로 빠르게 수행
import sys
data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
reach = [0] * (n + 1)  # reach[a]의 j번째 비트: a에서 j로 도달 가능
for i in range(m):
    a, b = int(data[2 + 2 * i]), int(data[3 + 2 * i])
    reach[a] |= 1 << b
for k in range(1, n + 1):
    rk = reach[k]
    bit = 1 << k
    for a in range(1, n + 1):
        if reach[a] & bit:
            reach[a] |= rk
rev = [0] * (n + 1)
for a in range(1, n + 1):
    r = reach[a]
    for b in range(1, n + 1):
        if r >> b & 1:
            rev[b] |= 1 << a
result = 0
full = ((1 << (n + 1)) - 2)
for i in range(1, n + 1):
    if (reach[i] | rev[i] | (1 << i)) == full:
        result += 1
print(result)
