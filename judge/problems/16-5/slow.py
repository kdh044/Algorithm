# 1부터 차례대로 모든 정수가 못생긴 수인지 직접 확인하는 풀이
n = int(input())
count = 0
x = 0
while count < n:
    x += 1
    y = x
    for p in (2, 3, 5):
        while y % p == 0:
            y //= p
    if y == 1:
        count += 1
print(x)
