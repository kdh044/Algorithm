# 저자 풀이와 같은 방식: 축별로 정렬해 인접한 행성끼리의 간선 3(N-1)개만 두고 크루스칼
# 빠른 입력, 간선을 정수 하나로 인코딩해 정렬, 반복문 find(경로 절반 압축) 사용
import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    if n == 1:
        print(0)
        return
    coords = [list(map(int, data[1 + k::3][:n])) for k in range(3)]
    SH = 19  # 간선 수 3(N-1) < 2^19, 비용 < 2^31 -> 50비트 정수 하나로 인코딩
    EA = []
    EB = []
    edges = []
    for c in coords:
        idx = sorted(range(n), key=c.__getitem__)
        prev = idx[0]
        pc = c[prev]
        for i in idx[1:]:
            ci = c[i]
            edges.append(((ci - pc) << SH) | len(EA))
            EA.append(prev)
            EB.append(i)
            prev, pc = i, ci
    edges.sort()
    parent = list(range(n))
    mask = (1 << SH) - 1
    total = 0
    cnt = 0
    for e in edges:
        k = e & mask
        a = EA[k]
        b = EB[k]
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        while parent[b] != b:
            parent[b] = parent[parent[b]]
            b = parent[b]
        if a != b:
            if a < b:
                parent[b] = a
            else:
                parent[a] = b
            total += e >> SH
            cnt += 1
            if cnt == n - 1:
                break
    print(total)


main()
