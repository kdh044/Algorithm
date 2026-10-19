# 저자 답안(9-5)과 같은 우선순위 큐 다익스트라. 입력을 한 번에 읽고 함수 안에서 실행해 상수만 줄인 버전
import heapq
import sys


def main():
    data = sys.stdin.buffer.read().split()
    INF = int(1e9)
    n, m, start = int(data[0]), int(data[1]), int(data[2])
    graph = [[] for _ in range(n + 1)]
    for i in range(3, 3 + 3 * m, 3):
        graph[int(data[i])].append((int(data[i + 1]), int(data[i + 2])))

    distance = [INF] * (n + 1)
    q = [(0, start)]
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for y, z in graph[now]:
            cost = dist + z
            if cost < distance[y]:
                distance[y] = cost
                heapq.heappush(q, (cost, y))

    count = 0
    max_distance = 0
    for d in distance:
        if d != INF:
            count += 1
            if d > max_distance:
                max_distance = d
    print(count - 1, max_distance)


main()
