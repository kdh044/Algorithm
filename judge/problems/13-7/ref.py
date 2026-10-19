# 저자 풀이와 같은 BFS 시뮬레이션이지만, 매일 전체를 훑는 대신
# "전날 인구가 바뀐 나라"에서만 연합 탐색을 시작하도록 최적화한 버전.
# (전날 바뀌지 않은 두 나라 사이의 국경은 전날과 상태가 같고, 전날 열려 있었다면
#  같은 연합이라 인구가 같아졌으므로 오늘은 닫혀 있다 -> 열리는 국경에는 반드시
#  전날 바뀐 나라가 끼어 있음)
import sys

def main():
    data = sys.stdin.buffer.read().split()
    n, l, r = int(data[0]), int(data[1]), int(data[2])
    W = n + 2
    # 패딩: 바깥은 -1000 (어떤 나라와도 차이가 R보다 큼)
    a = [-1000] * (W * W)
    for i in range(n):
        for j in range(n):
            a[(i + 1) * W + j + 1] = int(data[3 + i * n + j])
    cand = [(i + 1) * W + j + 1 for i in range(n) for j in range(n)]
    dirs = (1, -1, W, -W)
    mark = [0] * (W * W)
    day = 0
    while True:
        day += 1
        moved = False
        changed = []
        for s in cand:
            if mark[s] == day:
                continue
            mark[s] = day
            stack = [s]
            united = [s]
            total = a[s]
            while stack:
                u = stack.pop()
                au = a[u]
                for d in dirs:
                    v = u + d
                    if mark[v] != day:
                        diff = a[v] - au
                        if diff < 0:
                            diff = -diff
                        if l <= diff <= r:
                            mark[v] = day
                            stack.append(v)
                            united.append(v)
                            total += a[v]
            if len(united) > 1:
                moved = True
                avg = total // len(united)
                for u in united:
                    if a[u] != avg:
                        a[u] = avg
                        changed.append(u)
        if not moved:
            break
        cand = changed
    print(day - 1)

main()
