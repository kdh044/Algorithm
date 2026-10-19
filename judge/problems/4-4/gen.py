def generate(rng):
    cases = []

    def case(name, g, a, b, d):
        n, m = len(g), len(g[0])
        assert 3 <= n <= 50 and 3 <= m <= 50 and g[a][b] == 0
        assert all(g[0][j] == 1 and g[n - 1][j] == 1 for j in range(m))
        assert all(g[i][0] == 1 and g[i][m - 1] == 1 for i in range(n))
        s = f"{n} {m}\n{a} {b} {d}\n" + "".join(" ".join(map(str, r)) + "\n" for r in g)
        cases.append({"name": name, "input": s})

    def border(n, m, fill):
        g = [[fill(i, j) for j in range(m)] for i in range(n)]
        for i in range(n):
            g[i][0] = g[i][m - 1] = 1
        for j in range(m):
            g[0][j] = g[n - 1][j] = 1
        return g

    def rand_map(n, m, p):
        g = border(n, m, lambda i, j: 1 if rng.random() < p else 0)
        lands = [(i, j) for i in range(n) for j in range(m) if g[i][j] == 0]
        if not lands:
            g[1][1] = 0
            lands = [(1, 1)]
        a, b = rng.choice(lands)
        return g, a, b

    case("최소 3x3 육지 1칸", border(3, 3, lambda i, j: 0), 1, 1, 2)
    for d in range(4):
        case(f"전부 육지 방향 {d}", border(6, 7, lambda i, j: 0), 2, 3, d)
    g = border(5, 9, lambda i, j: 0)
    for j in range(1, 8):
        if j != 4:
            g[2][j] = 1
    case("좁은 통로 후진", g, 1, 1, 1)
    for i in range(8):
        n, m = rng.randint(3, 10), rng.randint(3, 10)
        g, a, b = rand_map(n, m, rng.choice([0.1, 0.3, 0.5]))
        case(f"작은 랜덤 {i+1}", g, a, b, rng.randrange(4))
    case("최대 전부 육지", border(50, 50, lambda i, j: 0), 25, 25, 0)
    case("최대 전부 육지 구석 시작", border(50, 50, lambda i, j: 0), 1, 48, 3)
    case("최대 체크 무늬", border(50, 50, lambda i, j: (i + j) % 2), 2, 2, 1)
    for i, p in enumerate([0.15, 0.3, 0.45]):
        g, a, b = rand_map(50, 50, p)
        case(f"최대 랜덤 {i+1}", g, a, b, rng.randrange(4))
    g = border(50, 50, lambda i, j: 1 if (i % 4 == 2 and j != (1 if i % 8 == 2 else 48)) else 0)
    case("최대 지그재그 통로", g, 1, 1, 1)
    return cases
