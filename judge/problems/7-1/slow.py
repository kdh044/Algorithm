# 정렬 없이 리스트에서 순차 탐색하는 O(N*M) 풀이
n = int(input())
array = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
out = []
for i in x:
    found = False
    for v in array:
        if v == i:
            found = True
            break
    out.append('yes' if found else 'no')
print(' '.join(out))
