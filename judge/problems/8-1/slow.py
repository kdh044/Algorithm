# 방문 처리를 빠뜨린 BFS: 1에서 출발해 +1, *2, *3, *5로 X를 찾는다.
# 같은 수를 여러 번 큐에 넣으므로 큐 크기가 단계마다 몇 배씩 불어나 지수 시간
from collections import deque

x = int(input())
q = deque([(1, 0)])
while q:
    v, d = q.popleft()
    if v == x:
        print(d)
        break
    for nv in (v + 1, v * 2, v * 3, v * 5):
        if nv <= x:
            q.append((nv, d + 1))
