# 방문 처리를 빠뜨린 BFS: 0원에서 출발해 화폐를 하나씩 더해 M원을 찾는다.
# 같은 금액을 여러 번 큐에 넣으므로 큐 크기가 단계마다 몇 배씩 불어나 지수 시간
from collections import deque

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]
q = deque([(0, 0)])
answer = -1
while q:
    v, d = q.popleft()
    if v == m:
        answer = d
        break
    for c in array:
        if v + c <= m:
            q.append((v + c, d + 1))
print(answer)
