# 저자 답안(9-4)의 플로이드 워셜.
# 원본은 입력받은 k를 플로이드 워셜 반복문 변수 k가 덮어써서 graph[1][n] + graph[n][x]를
# 출력하는 버그가 있으므로 반복문 변수를 바꿔 고쳤고, 가장 안쪽 반복을 리스트 컴프리헨션으로 바꿔 속도를 높였다.
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    graph[a][a] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for mid in range(1, n + 1):
    gm = graph[mid]
    for a in range(1, n + 1):
        ga = graph[a]
        d = ga[mid]
        if d >= INF:
            continue
        graph[a] = [u if u <= d + v else d + v for u, v in zip(ga, gm)]

distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)
