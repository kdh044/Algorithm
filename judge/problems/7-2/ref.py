# 저자 답안(7-8)과 같은 파라메트릭 서치이지만, 매번 N개를 순회하는 대신
# 정렬 + 누적합 + bisect로 '잘린 떡의 합'을 O(log N)에 계산하도록 바꾼 빠른 버전
import sys
from bisect import bisect_right
from itertools import accumulate

data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
array = sorted(map(int, data[2:2 + n]))
prefix = [0] + list(accumulate(array))
total_sum = prefix[-1]


def cut(h):
    j = bisect_right(array, h)  # h보다 큰 떡: array[j:]
    return (total_sum - prefix[j]) - h * (n - j)


start, end = 0, array[-1]
result = 0
while start <= end:
    mid = (start + end) // 2
    if cut(mid) < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
