# 메모이제이션 없이 삽입/삭제/교체로 갈 수 있는 모든 경우를 탐색하는 지수 시간 풀이
# (PyPy는 재귀 깊이가 수천 단계에서 막히므로 재귀 대신 스택으로 같은 탐색을 수행)
str1 = input().strip()
str2 = input().strip()
n, m = len(str1), len(str2)

best = n + m
stack = [(0, 0, 0)]
while stack:
    i, j, c = stack.pop()
    while i < n and j < m and str1[i] == str2[j]:
        i += 1
        j += 1
    if i == n or j == m:
        c += (m - j) + (n - i)
        if c < best:
            best = c
        continue
    stack.append((i + 1, j + 1, c + 1))
    stack.append((i + 1, j, c + 1))
    stack.append((i, j + 1, c + 1))
print(best)
