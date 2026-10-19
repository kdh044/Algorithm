# 매번 앞쪽 덩어리를 잘라낸 새 문자열을 만드는 O(N^2) 풀이
s = input()
groups = {'0': 0, '1': 0}
while s:
    c = s[0]
    i = 1
    while i < len(s) and s[i] == c:
        i += 1
    groups[c] += 1
    s = s[i:]
print(min(groups['0'], groups['1']))
