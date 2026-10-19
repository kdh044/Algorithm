# 저자 풀이(크루스칼)와 동일한 결과를 내는 빠른 버전
# 빠른 입력, 간선을 정수 하나로 인코딩해 정렬, 반복문 find(경로 절반 압축) 사용
import sys


def main():
    vals = list(map(int, sys.stdin.buffer.read().split()))
    n, m = vals[0], vals[1]
    xs = vals[2::3]
    ys = vals[3::3]
    zs = vals[4::3]
    parent = list(range(n))
    keys = [(z << 36) | (x << 18) | y for x, y, z in zip(xs, ys, zs)]
    keys.sort()
    mask = (1 << 18) - 1
    mst = 0
    need = n - 1
    for k in keys:
        if not need:
            break
        a = (k >> 18) & mask
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        b = k & mask
        while parent[b] != b:
            parent[b] = parent[parent[b]]
            b = parent[b]
        if a != b:
            if a < b:
                parent[b] = a
            else:
                parent[a] = b
            mst += k >> 36
            need -= 1
    print(sum(zs) - mst)


main()
