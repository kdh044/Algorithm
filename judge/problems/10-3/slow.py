# 메모이제이션 없는 재귀: 강의 i까지의 최소 시간 = time[i] + max(선수 강의들의 최소 시간) -> 지수 시간
n = int(input())
time = [0] * (n + 1)
pre = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    pre[i] = data[1:-1]


def f(i):
    best = 0
    for p in pre[i]:
        best = max(best, f(p))
    return best + time[i]


for i in range(1, n + 1):
    print(f(i))
