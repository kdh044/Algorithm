# 저자 코드와 같은 2차원 DP(왼쪽 위 / 왼쪽 / 왼쪽 아래 중 최댓값 + 현재 칸).
# T=1000, 20x20 최대 입력에서 시간 여유를 위해 입력을 한 번에 읽고 열 단위로 계산하도록 다듬었다.
import sys

data = sys.stdin.buffer.read().split()
pos = 0
t = int(data[pos]); pos += 1
out = []
for tc in range(t):
    n, m = int(data[pos]), int(data[pos + 1]); pos += 2
    array = list(map(int, data[pos:pos + n * m])); pos += n * m
    # prev[i]: 이전 열의 i행까지 얻을 수 있는 금의 최댓값
    prev = [array[i * m] for i in range(n)]
    for j in range(1, m):
        cur = [0] * n
        for i in range(n):
            best = prev[i]
            if i > 0 and prev[i - 1] > best:
                best = prev[i - 1]
            if i < n - 1 and prev[i + 1] > best:
                best = prev[i + 1]
            cur[i] = array[i * m + j] + best
        prev = cur
    out.append(max(prev))
print("\n".join(map(str, out)))
