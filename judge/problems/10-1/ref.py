# 저자 답안(10-7)과 같은 경로 압축 서로소 집합.
# 빠른 입력, 반복문 find(재귀 한도 문제 없음), 출력 모으기로 상수만 줄인 버전
import sys


def find_parent(parent, x):
    root = x
    while parent[root] != root:
        root = parent[root]
    while parent[x] != root:
        parent[x], x = root, parent[x]
    return root


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
parent = list(range(n + 1))
out = []
it = iter(map(int, data[2:2 + 3 * m]))
for oper, a, b in zip(it, it, it):
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        out.append('YES' if find_parent(parent, a) == find_parent(parent, b) else 'NO')
print('\n'.join(out))
