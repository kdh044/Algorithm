# 서로 다른 모든 후보 위치마다 거리의 합을 직접 계산하는 O(N^2) 풀이
n = int(input())
a = list(map(int, input().split()))
best = None
answer = None
for p in sorted(set(a)):
    total = 0
    for x in a:
        total += abs(x - p)
    if best is None or total < best:
        best = total
        answer = p
print(answer)
