# 메모이제이션 없는 재귀 -> 지수 시간
import sys
sys.setrecursionlimit(10000)


def f(n):
    if n <= 1:
        return 1
    return (f(n - 1) + 2 * f(n - 2)) % 796796


print(f(int(input())))
