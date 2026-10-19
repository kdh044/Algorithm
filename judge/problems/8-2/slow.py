# 메모이제이션 없는 재귀 -> 피보나치처럼 지수 시간
n = int(input())
array = list(map(int, input().split()))


def f(i):
    if i < 0:
        return 0
    return max(f(i - 1), f(i - 2) + array[i])


print(f(n - 1))
