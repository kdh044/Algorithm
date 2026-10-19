# 거리를 1부터 하나씩 늘려 가며 확인하는 O(N * 답) 풀이
n, c = map(int, input().split())
array = sorted(int(input()) for _ in range(n))

def possible(gap):
    count = 1
    value = array[0]
    for x in array:
        if x >= value + gap:
            value = x
            count += 1
    return count >= c

gap = 1
while possible(gap + 1):
    gap += 1
print(gap)
