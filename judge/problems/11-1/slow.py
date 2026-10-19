# 매번 최솟값을 찾아 빼는 O(N^2) 풀이
n = int(input())
data = list(map(int, input().split()))
result = 0
count = 0
while data:
    m = min(data)
    data.remove(m)
    count += 1
    if count >= m:
        result += 1
        count = 0
print(result)
