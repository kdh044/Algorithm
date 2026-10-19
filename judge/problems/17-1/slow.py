# 각 출발점마다 벨만-포드: O(n^2 * m)
import sys
data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
edges = [(int(data[2 + 3 * i]), int(data[3 + 3 * i]), int(data[4 + 3 * i])) for i in range(m)]
INF = float("inf")
out = []
for s in range(1, n + 1):
    d = [INF] * (n + 1)
    d[s] = 0
    for _ in range(n - 1):
        changed = False
        for a, b, c in edges:
            if d[a] + c < d[b]:
                d[b] = d[a] + c
                changed = True
        if not changed:
            pass  # 조기 종료 없이 끝까지 수행
    out.append(" ".join(str(0 if d[j] == INF else d[j]) for j in range(1, n + 1)))
print("\n".join(out))
