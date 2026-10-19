# 저자 풀이(모든 조합 완전 탐색)와 동일한 방식이지만,
# 치킨집별로 "각 집까지의 거리" 리스트를 미리 구해 두고
# 조합마다 원소별 최솟값(map(min, ...))으로 빠르게 합을 구한다.
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))  # 일반 집
        elif data[c] == 2:
            chicken.append((r, c))  # 치킨집

dist = [[abs(hx - cx) + abs(hy - cy) for hx, hy in house] for cx, cy in chicken]

result = int(1e9)
for candidate in combinations(range(len(chicken)), m):
    result = min(result, sum(map(min, *[dist[i] for i in candidate])) if m > 1 else sum(dist[candidate[0]]))

print(result)
