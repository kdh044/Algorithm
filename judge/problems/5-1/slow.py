# 라벨 전파: 모든 칸을 반복해서 훑으며 이웃의 최소 라벨로 갱신 (수렴까지 O(NM * 경로 길이))
n, m = map(int, input().split())
g = [input() for _ in range(n)]
INF = n * m + 1
lab = [[(i * m + j) if g[i][j] == '0' else INF for j in range(m)] for i in range(n)]
changed = True
while changed:
    changed = False
    for i in range(n):
        for j in range(m):
            if g[i][j] != '0':
                continue
            v = lab[i][j]
            if i > 0 and lab[i - 1][j] < v:
                v = lab[i - 1][j]
            if i < n - 1 and lab[i + 1][j] < v:
                v = lab[i + 1][j]
            if j > 0 and lab[i][j - 1] < v:
                v = lab[i][j - 1]
            if j < m - 1 and lab[i][j + 1] < v:
                v = lab[i][j + 1]
            if v < lab[i][j]:
                lab[i][j] = v
                changed = True
print(sum(1 for i in range(n) for j in range(m) if g[i][j] == '0' and lab[i][j] == i * m + j))
