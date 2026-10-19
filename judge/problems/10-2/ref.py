# 저자 답안(10-8)과 같은 크루스칼(최소 신장 트리 - 가장 큰 간선).
# 입력이 최대 100만 줄(약 15MB)이라 PyPy에서도 split/int 변환이 병목이 되므로 바이트를 직접 읽어 정수로 바꾸고,
# 유지비가 1000 이하인 점을 이용해 계수 정렬로 간선을 정렬한다. find는 반복문(경로 절반 압축),
# N-1개를 고르면 멈춘다.
import sys


def main():
    data = sys.stdin.buffer.read()
    vals = []
    ap = vals.append
    x = 0
    innum = False
    for c in data:
        if c >= 48:
            x = x * 10 + c - 48
            innum = True
        elif innum:
            ap(x)
            x = 0
            innum = False
    if innum:
        ap(x)
    v, e = vals[0], vals[1]
    cnt = [0] * 1002
    for i in range(e):
        cnt[vals[4 + 3 * i]] += 1
    pos = [0] * 1002
    s = 0
    for c in range(1002):
        pos[c] = s
        s += cnt[c]
    order = [0] * e
    for i in range(e):
        c = vals[4 + 3 * i]
        order[pos[c]] = i
        pos[c] += 1

    parent = list(range(v + 1))
    result = 0
    last = 0
    picked = 0
    for i in order:
        k = 2 + 3 * i
        a = vals[k]
        b = vals[k + 1]
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
            cost = vals[k + 2]
            result += cost
            last = cost
            picked += 1
            if picked == v - 1:
                break
    print(result - last)


main()
