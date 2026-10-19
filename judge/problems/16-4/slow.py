# 메모이제이션 없이 "i번째 병사부터 시작하는 가장 긴 감소 부분 수열"을 재귀로 구하는 지수 시간 풀이
import sys
sys.setrecursionlimit(10000)

n = int(input())
array = list(map(int, input().split()))


def longest(i):
    best = 1
    for j in range(i + 1, n):
        if array[j] < array[i]:
            best = max(best, 1 + longest(j))
    return best


print(n - max(longest(i) for i in range(n)))
