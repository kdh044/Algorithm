# 위상 정렬의 매 단계마다 남은 노드의 진입차수를 처음부터 다시 계산: O(n^3)
import sys
data = sys.stdin.buffer.read().split()
pos = 0
T = int(data[pos]); pos += 1
out = []
for _ in range(T):
    n = int(data[pos]); pos += 1
    last = [int(x) for x in data[pos:pos + n]]; pos += n
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            graph[last[i]][last[j]] = True
    m = int(data[pos]); pos += 1
    for _ in range(m):
        a, b = int(data[pos]), int(data[pos + 1]); pos += 2
        graph[a][b], graph[b][a] = graph[b][a], graph[a][b]
    removed = [False] * (n + 1)
    result = []
    state = "ok"
    for _ in range(n):
        zeros = []
        for v in range(1, n + 1):
            if removed[v]:
                continue
            indeg = 0
            for u in range(1, n + 1):
                if not removed[u] and graph[u][v]:
                    indeg += 1
            if indeg == 0:
                zeros.append(v)
        if not zeros:
            state = "cycle"
            break
        if len(zeros) >= 2:
            state = "multi"
            break
        removed[zeros[0]] = True
        result.append(zeros[0])
    if state == "cycle":
        out.append("IMPOSSIBLE")
    elif state == "multi":
        out.append("?")
    else:
        out.append(" ".join(map(str, result)))
print("\n".join(out))
