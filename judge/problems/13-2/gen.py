def generate(rng):
    cases = []

    def case(name, grid):
        n, m = len(grid), len(grid[0])
        lines = [f"{n} {m}"] + [" ".join(map(str, r)) for r in grid]
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    def rand_grid(n, m, viruses, wall_p):
        while True:
            g = [[1 if rng.random() < wall_p else 0 for _ in range(m)] for _ in range(n)]
            pos = [(i, j) for i in range(n) for j in range(m)]
            rng.shuffle(pos)
            for i, j in pos[:viruses]:
                g[i][j] = 2
            if sum(r.count(0) for r in g) >= 3:
                return g

    # 최소: 3x3, 빈칸이 정확히 3개
    case("최소 3x3 빈칸 3개", [[2, 1, 0], [1, 1, 0], [2, 1, 0]])
    case("빈칸 3개 모두 막힘", [[2, 0, 1], [0, 1, 1], [2, 0, 1]])
    case("벽 없이 3x3", [[2, 0, 0], [0, 0, 0], [0, 0, 2]])
    case("바이러스가 이미 갇힘", [[2, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 2]])
    case("바이러스 10개", [[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    for i in range(7):
        n, m = rng.randint(3, 8), rng.randint(3, 8)
        case(f"작은 랜덤 {i+1}", rand_grid(n, m, rng.randint(2, min(10, n * m - 3)), rng.choice([0.1, 0.2, 0.3, 0.4])))
    # 큰 케이스: 빈칸 54개(책 예제 3과 같은 수). 벽이 전혀 없는 8x8(빈칸 62개)은 저자 풀이
    # (벽 3개를 순서 있는 조합으로 모두 시도: 62*61*60가지)가 PyPy에서도 2초를 넘겨 빈칸 수를 맞췄다.
    g = [[0] * 8 for _ in range(8)]
    g[0][0] = g[7][7] = 2
    for i, j in [(2, 5), (5, 2), (1, 6), (6, 1), (3, 3), (4, 4), (2, 2), (5, 5)]:
        g[i][j] = 1
    case("8x8 벽 8개 바이러스 2개(모서리)", g)
    g = [[0] * 8 for _ in range(8)]
    g[3][3] = g[4][4] = 2
    for i, j in [(0, 3), (0, 4), (7, 3), (7, 4), (3, 0), (4, 0), (3, 7), (4, 7)]:
        g[i][j] = 1
    case("8x8 벽 8개 바이러스 2개(중앙)", g)
    g = [[0] * 8 for _ in range(8)]
    for i, j in [(0, 0), (0, 7), (7, 0), (7, 7), (3, 3), (4, 4), (0, 4), (7, 3), (4, 0), (3, 7)]:
        g[i][j] = 2
    case("8x8 바이러스 10개 흩어짐", g)
    # 미로 형태 (확산 경로가 길어짐)
    g = [[0] * 8 for _ in range(8)]
    for i in range(1, 8, 2):
        for j in range(8):
            g[i][j] = 1
        g[i][7 if i % 4 == 1 else 0] = 0
    g[0][0] = 2
    g[6][0] = 2
    case("8x8 지그재그 통로", g)
    for i in range(3):
        case(f"8x8 랜덤 {i+1}", rand_grid(8, 8, rng.randint(2, 10), rng.choice([0.05, 0.15, 0.25])))
    return cases
