# 삽입 정렬 O(N^2) (안정 정렬)
n = int(input())
array = []
for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))
for i in range(1, n):
    j = i
    while j > 0 and array[j - 1][1] > array[j][1]:
        array[j - 1], array[j] = array[j], array[j - 1]
        j -= 1
print(' '.join(s[0] for s in array))
