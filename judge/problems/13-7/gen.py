def count_moves(g, l, r):
    # 단순 시뮬레이션 (입력 조건 '이동 횟수 <= 2000' 확인용)
    n = len(g)
    a = [row[:] for row in g]
    days = 0
    while True:
        seen = [[False] * n for _ in range(n)]
        moved = False
        for i in range(n):
            for j in range(n):
                if seen[i][j]:
                    continue
                seen[i][j] = True
                st, un = [(i, j)], [(i, j)]
                while st:
                    x, y = st.pop()
                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= nx < n and 0 <= ny < n and not seen[nx][ny] and l <= abs(a[nx][ny] - a[x][y]) <= r:
                            seen[nx][ny] = True
                            st.append((nx, ny))
                            un.append((nx, ny))
                if len(un) > 1:
                    moved = True
                    avg = sum(a[x][y] for x, y in un) // len(un)
                    for x, y in un:
                        a[x][y] = avg
        if not moved:
            return days
        days += 1


def snake_path(n, by_col=False):
    # 짝수 번째 줄을 지그재그로 잇는 경로 (홀수 줄은 연결 칸 하나만 사용)
    path = []
    for r in range(0, n, 2):
        cols = range(n) if (r // 2) % 2 == 0 else range(n - 1, -1, -1)
        for c in cols:
            path.append((r, c))
        if r + 2 < n:
            path.append((r + 1, n - 1 if (r // 2) % 2 == 0 else 0))
    if by_col:
        path = [(c, r) for r, c in path]
    return path


def generate(rng):
    cases = []

    def case(name, g, l, r, check=True):
        n = len(g)
        assert 1 <= n <= 50 and 1 <= l <= r <= 100
        assert all(0 <= v <= 100 for row in g for v in row)
        if check:
            assert count_moves(g, l, r) <= 2000
        lines = [f"{n} {l} {r}"] + [" ".join(map(str, row)) for row in g]
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    def rand_grid(n, lo, hi):
        return [[rng.randint(lo, hi) for _ in range(n)] for _ in range(n)]

    case("N=1", [[37]], 1, 100)
    case("전부 같은 인구", [[50] * 5 for _ in range(5)], 1, 100)
    case("차이가 모두 R 초과", [[0, 100], [100, 0]], 1, 99)
    case("차이가 정확히 L=R", [[0, 7], [7, 0]], 7, 7)
    case("인구 0과 100", [[0, 100, 0], [100, 0, 100], [0, 100, 0]], 1, 100)
    for i in range(6):
        n = rng.randint(2, 10)
        l = rng.randint(1, 30)
        case(f"작은 랜덤 {i+1}", rand_grid(n, 0, 100), l, rng.randint(l, 60))
    for i in range(3):
        l = rng.randint(1, 20)
        case(f"최대 N 랜덤 {i+1}", rand_grid(50, 0, 100), l, rng.randint(l, 50))
    case("최대 N 좁은 범위 랜덤", rand_grid(50, 40, 60), 1, 3)
    case("최대 N 체스판", [[100 if (i + j) % 2 else 0 for j in range(50)] for i in range(50)], 1, 100)

    # 이동 횟수가 많은 최악 케이스: 뱀 모양 경로를 따라 하루에 한 칸씩 연합이 전진
    # (경로 밖 칸은 인구 차이가 R보다 커서 항상 국경이 닫혀 있음)
    def snake_case(name, n, l, r, start, up, down, wall, by_col=False):
        g = [[wall] * n for _ in range(n)]
        for p, (x, y) in enumerate(snake_path(n, by_col)):
            g[x][y] = start if p == 0 else (up if p % 2 else down)
        case(name, g, l, r)

    snake_case("최대 N 뱀 경로 (이동 1273번)", 50, 2, 2, 10, 12, 9, 0)
    snake_case("최대 N 세로 뱀 경로", 50, 3, 5, 50, 54, 48, 100, by_col=True)
    snake_case("N=49 뱀 경로", 49, 2, 2, 90, 92, 89, 30)
    # 여러 줄에서 동시에 전진 + 나머지는 랜덤
    g = [[rng.randint(70, 100) for _ in range(50)] for _ in range(50)]
    for x in range(0, 50, 2):
        for y in range(50):
            g[x][y] = 10 if y == 0 else (12 if y % 2 else 9)
        if x + 1 < 50:
            g[x + 1] = [0] * 50
    case("최대 N 여러 줄 동시 전진", g, 2, 2)
    return cases
