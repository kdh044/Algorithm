# 매번 A의 최솟값과 B의 최댓값을 선형 탐색으로 찾아 교체: O(NK)
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for _ in range(k):
    i = min(range(n), key=a.__getitem__)
    j = max(range(n), key=b.__getitem__)
    if a[i] < b[j]:
        a[i], b[j] = b[j], a[i]
    else:
        break
print(sum(a))
