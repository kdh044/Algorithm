# 저자 코드(이진 탐색 + 그리디 설치)와 같은 방식.
# 파이썬에서 시간 여유를 위해 입력을 한 번에 읽고, 탐색 상한을 (끝-처음)//(C-1)로 줄였으며,
# C가 작을 때는 다음 설치 위치를 bisect로 바로 찾는다.
import sys
from bisect import bisect_left

data = sys.stdin.buffer.read().split()
n, c = int(data[0]), int(data[1])
array = sorted(map(int, data[2:2 + n]))


def possible_loop(gap):
    count = 1
    target = array[0] + gap
    for x in array:
        if x >= target:
            count += 1
            target = x + gap
    return count >= c


def possible_bisect(gap):
    count = 1
    i = 0
    value = array[0]
    while count < c:
        i = bisect_left(array, value + gap, i + 1)
        if i >= n:
            return False
        value = array[i]
        count += 1
    return True


possible = possible_bisect if c * 8 < n else possible_loop

start = 1
end = (array[-1] - array[0]) // (c - 1)
result = 0
while start <= end:
    mid = (start + end) // 2
    if possible(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
