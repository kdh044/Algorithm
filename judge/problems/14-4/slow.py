# 매번 리스트에서 가장 작은 두 묶음을 선형 탐색으로 찾는 O(N^2) 풀이
n = int(input())
data = [int(input()) for _ in range(n)]
result = 0
while len(data) > 1:
    a = min(data)
    data.remove(a)
    b = min(data)
    data.remove(b)
    result += a + b
    data.append(a + b)
print(result)
