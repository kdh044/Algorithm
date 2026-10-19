# 메모이제이션 없이 모든 경로를 탐색하는 O(2^n) 풀이
import sys
sys.setrecursionlimit(10000)

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]


def go(i, j):
    if i == n - 1:
        return tri[i][j]
    return tri[i][j] + max(go(i + 1, j), go(i + 1, j + 1))


print(go(0, 0))
