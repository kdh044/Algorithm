from itertools import combinations
import math

def solution(n, m, city):
    houses = []
    chickens = []

    for r in range(n):
        for c in range(n):
            if city[r][c] == 1:
                houses.append((r + 1, c + 1))
            elif city[r][c] == 2:
                chickens.append((r + 1, c + 1))

    answer = math.inf

    for selected in combinations(chickens, m):
        total = 0

        for hr, hc in houses:
            min_dist = math.inf

            for cr, cc in selected:
                distance = abs(hr - cr) + abs(hc - cc)
                min_dist = min(min_dist, distance)

            total += min_dist

        answer = min(answer, total)

    return answer


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, m, city))