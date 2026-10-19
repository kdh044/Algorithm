def generate(rng):
    cases = []

    def case(name, g):
        n, m = len(g), len(g[0])
        assert 4 <= n <= 200 and 4 <= m <= 200 and g[0][0] == 1 and g[n - 1][m - 1] == 1
        cases.append({"name": name, "input": f"{n} {m}\n" + "".join("".join(map(str, r)) + "\n" for r in g)})

    def carve_path(g):
        # (0,0)에서 (n-1,m-1)까지 무작위 경로를 뚫어 탈출 가능 보장
        n, m = len(g), len(g[0])
        x = y = 0
        g[0][0] = 1
        while (x, y) != (n - 1, m - 1):
            r = rng.random()
            if r < 0.4 and x < n - 1:
                x += 1
            elif r < 0.8 and y < m - 1:
                y += 1
            elif r < 0.9 and x > 0:
                x -= 1
            elif y > 0:
                y -= 1
            g[x][y] = 1
        return g

    def rand_maze(n, m, p):
        g = [[1 if rng.random() < p else 0 for _ in range(m)] for _ in range(n)]
        return carve_path(g)

    def snake(n, m):
        g = []
        for i in range(n):
            if i % 2 == 0 or i >= n - 2:
                g.append([1] * m)
            else:
                gap = m - 1 if i % 4 == 1 else 0
                g.append([1 if j == gap else 0 for j in range(m)])
        return g

    case("최소 4x4 전부 1", [[1] * 4 for _ in range(4)])
    g = [[0] * 4 for _ in range(4)]
    for j in range(4):
        g[0][j] = 1
    for i in range(4):
        g[i][3] = 1
    case("최소 4x4 외길", g)
    case("뱀 모양 작게", snake(9, 6))
    for i in range(8):
        n, m = rng.randint(4, 15), rng.randint(4, 15)
        case(f"작은 랜덤 {i+1}", rand_maze(n, m, rng.choice([0.4, 0.6, 0.8])))
    case("최대 전부 1", [[1] * 200 for _ in range(200)])
    case("최대 랜덤", rand_maze(200, 200, 0.6))
    case("최대 랜덤 빽빽", rand_maze(200, 200, 0.75))
    case("최대 뱀 모양", snake(200, 200))
    g = snake(200, 200)
    g = [list(r) for r in zip(*g)]
    case("최대 세로 뱀 모양", g)
    return cases
