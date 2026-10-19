# 저자 풀이(플로이드 워셜)와 동일한 결과를 내는 빠른 버전
import sys
INF = int(1e9)
data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    graph[a][a] = 0
idx = 2
for _ in range(m):
    a, b, c = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
    idx += 3
    if c < graph[a][b]:
        graph[a][b] = c
for k in range(1, n + 1):
    gk = graph[k]
    for a in range(1, n + 1):
        ga = graph[a]
        dak = ga[k]
        if dak == INF:
            continue
        graph[a] = list(map(min, ga, [dak + x for x in gk]))
out = []
for a in range(1, n + 1):
    out.append(" ".join("0" if v >= INF else str(v) for v in graph[a][1:]))
print("\n".join(out))
