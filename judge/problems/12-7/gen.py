def generate(rng):
    cases = []
    def case(name, n, m, g):
        h = sum(r.count(1) for r in g)
        c = sum(r.count(2) for r in g)
        assert 2 <= n <= 50 and 1 <= m <= 13 and len(g) == n and all(len(r) == n for r in g)
        assert 1 <= h <= 2 * n and m <= c <= 13
        cases.append({"name": name, "input": f"{n} {m}\n" + "".join(" ".join(map(str, r)) + "\n" for r in g)})

    def rand_city(n, h, c, m=None):
        cells = rng.sample([(i, j) for i in range(n) for j in range(n)], h + c)
        g = [[0] * n for _ in range(n)]
        for i, j in cells[:h]:
            g[i][j] = 1
        for i, j in cells[h:]:
            g[i][j] = 2
        return g

    case("최소 N=2", 2, 1, [[1, 2], [0, 0]])
    case("N=2 꽉 참", 2, 2, [[1, 2], [2, 1]])
    case("집 1개, 치킨집 1개 멀리", 50, 1, [[1] + [0] * 49] + [[0] * 50 for _ in range(48)] + [[0] * 49 + [2]])
    case("M = 치킨집 수 = 13", 10, 13, rand_city(10, 20, 13))
    case("M=1, 치킨집 13개", 10, 1, rand_city(10, 20, 13))
    for i in range(6):
        n = rng.randint(3, 12)
        c = rng.randint(1, min(13, n * n - 1))
        h = rng.randint(1, min(2 * n, n * n - c))
        m = rng.randint(1, c)
        case(f"작은 랜덤 {i+1}", n, m, rand_city(n, h, c))
    n = 50
    for m in (6, 7):
        case(f"최대 N=50, 집 100, 치킨집 13, M={m}", n, m, rand_city(n, 100, 13))
    case("최대 N=50, M=13", n, 13, rand_city(n, 100, 13))
    case("최대 N=50, M=1", n, 1, rand_city(n, 100, 13))
    # 집이 한쪽에 몰린 경우
    g = [[0] * n for _ in range(n)]
    cells = rng.sample([(i, j) for i in range(10) for j in range(10)], 100)
    for i, j in cells:
        g[i][j] = 1
    for i, j in rng.sample([(i, j) for i in range(10, 50) for j in range(50)], 13):
        g[i][j] = 2
    case("최대, 집이 한 구석에 몰림 M=6", n, 6, g)
    return cases
