# 저자 풀이(BFS)와 동일한 알고리즘, 입력을 한 번에 읽도록만 바꾼 버전
import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    n, m, k, x = int(data[0]), int(data[1]), int(data[2]), int(data[3])
    graph = [[] for _ in range(n + 1)]
    for i in range(4, 4 + 2 * m, 2):
        graph[int(data[i])].append(int(data[i + 1]))
    distance = [-1] * (n + 1)
    distance[x] = 0
    q = deque([x])
    while q:
        now = q.popleft()
        d = distance[now] + 1
        for nxt in graph[now]:
            if distance[nxt] == -1:
                distance[nxt] = d
                q.append(nxt)
    res = [i for i in range(1, n + 1) if distance[i] == k]
    if res:
        sys.stdout.write("\n".join(map(str, res)) + "\n")
    else:
        print(-1)

main()
