# 저자 풀이와 동일(서로소 집합), 재귀 대신 반복문으로 find를 수행해 깊은 트리에서도 안전
import sys
data = sys.stdin.buffer.read().split()
g, p = int(data[0]), int(data[1])
parent = list(range(g + 1))

def find_parent(x):
    root = x
    while parent[root] != root:
        root = parent[root]
    while parent[x] != root:
        parent[x], x = root, parent[x]
    return root

result = 0
for i in range(p):
    root = find_parent(int(data[2 + i]))
    if root == 0:
        break
    # 바로 왼쪽의 집합과 합치기 (작은 번호가 루트)
    parent[root] = find_parent(root - 1)
    result += 1
print(result)
