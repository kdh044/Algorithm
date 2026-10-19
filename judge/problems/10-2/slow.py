# 크루스칼이지만 서로소 집합 대신 '집합 번호' 배열을 두고 합칠 때마다 전체를 다시 칠하는 O(N^2) 풀이
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
group = list(range(v + 1))
result = 0
last = 0
for c, a, b in edges:
    ga, gb = group[a], group[b]
    if ga != gb:
        for i in range(1, v + 1):
            if group[i] == gb:
                group[i] = ga
        result += c
        last = c
print(result - last)
