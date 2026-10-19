# 저자 풀이와 같은 완전 탐색(벽 3개의 모든 조합 + 바이러스 확산)을
# 비트마스크로 구현해 CPython에서도 빠르게 동작하도록 바꾼 버전
import sys
from itertools import combinations

def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    W = m + 1  # 각 행 끝에 벽 역할을 하는 패딩 열을 하나 둔다
    empty = 0
    virus = 0
    cells = []
    for i in range(n):
        for j in range(m):
            v = data[2 + i * m + j]
            bit = 1 << (i * W + j)
            if v == '0':
                empty |= bit
                cells.append(bit)
            elif v == '2':
                virus |= bit
    total = len(cells) - 3
    base = empty | virus
    best = 0
    for a, b, c in combinations(cells, 3):
        mask = base & ~(a | b | c)
        cur = virus
        while True:
            nxt = (cur | (cur << 1) | (cur >> 1) | (cur << W) | (cur >> W)) & mask
            if nxt == cur:
                break
            cur = nxt
        safe = total - (cur & empty).bit_count()
        if safe > best:
            best = safe
    print(best)

main()
