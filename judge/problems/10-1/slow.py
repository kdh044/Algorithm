# 경로 압축 없는 서로소 집합 -> 트리가 한쪽으로 길어지면 find가 O(N)
import sys
input = sys.stdin.readline


def find_parent(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = list(range(n + 1))
out = []
for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    else:
        out.append('YES' if find_parent(parent, a) == find_parent(parent, b) else 'NO')
print('\n'.join(out))
