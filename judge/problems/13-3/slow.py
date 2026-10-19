# 문제 문장을 그대로 따라 하는 시뮬레이션: 매 초마다 번호가 낮은 바이러스 종류부터 차례로,
# 시험관 전체를 훑어 그 종류의 칸을 찾아 증식시킨다. O(S * K * N^2) (S는 시험관이 다 찰 때까지만)
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
when = [[0] * n for _ in range(n)]
types = sorted(set(v for row in graph for v in row if v))
for sec in range(s):
    changed = False
    for v in types:
        for i in range(n):
            row = graph[i]
            for j in range(n):
                if row[j] == v and when[i][j] <= sec:
                    for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= ni < n and 0 <= nj < n and graph[ni][nj] == 0:
                            graph[ni][nj] = v
                            when[ni][nj] = sec + 1
                            changed = True
    if not changed:
        break
print(graph[x - 1][y - 1])
