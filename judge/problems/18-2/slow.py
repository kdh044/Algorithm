# 비행기마다 g_i번부터 1번까지 빈 탑승구를 선형 탐색: O(G * P)
import sys
data = sys.stdin.buffer.read().split()
g, p = int(data[0]), int(data[1])
used = [False] * (g + 1)
result = 0
for i in range(p):
    x = int(data[2 + i])
    while x > 0 and used[x]:
        x -= 1
    if x == 0:
        break
    used[x] = True
    result += 1
print(result)
