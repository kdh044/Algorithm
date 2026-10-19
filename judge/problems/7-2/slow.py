# 절단기 높이를 가장 긴 떡부터 1씩 낮춰 가며 확인하는 순차 탐색 O(N * max H)
n, m = map(int, input().split())
array = list(map(int, input().split()))
h = max(array)
while True:
    total = 0
    for x in array:
        if x > h:
            total += x - h
    if total >= m:
        print(h)
        break
    h -= 1
