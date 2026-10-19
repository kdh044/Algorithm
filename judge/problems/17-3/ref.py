# 저자 풀이(격자 다익스트라)와 동일한 결과를 내는 빠른 버전
# 칸 비용이 0~9뿐이므로 우선순위 큐 대신 거리별 버킷(Dial 알고리즘, 버킷 10개를 원형으로 사용)을 쓴다
import sys
data = sys.stdin.buffer.read().split()
pos = 0
t = int(data[pos]); pos += 1
out = []
for _ in range(t):
    n = int(data[pos]); pos += 1
    V = n * n
    cost = list(map(int, data[pos:pos + V])); pos += V
    INF = 1 << 60
    dist = [INF] * V
    dist[0] = cost[0]
    target = V - 1
    buckets = [[] for _ in range(10)]
    buckets[cost[0] % 10].append(0)
    d = cost[0]
    pending = 1
    while pending:
        b = buckets[d % 10]
        while b:
            u = b.pop()
            pending -= 1
            if dist[u] != d:
                continue
            r = u // n
            c = u - r * n
            if r > 0:
                v = u - n
                nd = d + cost[v]
                if nd < dist[v]:
                    dist[v] = nd
                    buckets[nd % 10].append(v)
                    pending += 1
            if r < n - 1:
                v = u + n
                nd = d + cost[v]
                if nd < dist[v]:
                    dist[v] = nd
                    buckets[nd % 10].append(v)
                    pending += 1
            if c > 0:
                v = u - 1
                nd = d + cost[v]
                if nd < dist[v]:
                    dist[v] = nd
                    buckets[nd % 10].append(v)
                    pending += 1
            if c < n - 1:
                v = u + 1
                nd = d + cost[v]
                if nd < dist[v]:
                    dist[v] = nd
                    buckets[nd % 10].append(v)
                    pending += 1
        d += 1
    out.append(str(dist[target]))
print("\n".join(out))
