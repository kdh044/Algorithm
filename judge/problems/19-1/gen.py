def generate(rng):
    cases = []

    def case(name, grid):
        n = len(grid)
        cases.append({"name": name, "input": f"{n}\n" + "\n".join(" ".join(map(str, r)) for r in grid) + "\n"})

    def rand_grid(n, density, sizes):
        g = [[(rng.choice(sizes) if rng.random() < density else 0) for _ in range(n)] for _ in range(n)]
        g[rng.randrange(n)][rng.randrange(n)] = 9
        return g

    case("N=2 먹을 것 없음", [[9, 2], [2, 3]])
    case("N=2 한 마리", [[9, 1], [0, 0]])
    case("큰 물고기에 갇힘", [[0, 1, 0], [3, 9, 3], [0, 3, 0]])
    case("같은 거리: 위쪽 우선", [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 9, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])
    case("같은 거리 같은 행: 왼쪽 우선", [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 9, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    case("같은 크기 물고기는 지나가기만", [[1, 2, 2, 2, 9], [0, 0, 0, 0, 0]] + [[0] * 5 for _ in range(3)])
    g = [[1] * 20 for _ in range(20)]
    g[0][0] = 9
    case("전부 크기 1 물고기", g)
    g = [[0] * 20 for _ in range(20)]
    g[10][10] = 9
    case("빈 공간", g)
    for i in range(6):
        n = rng.randint(2, 8)
        case(f"작은 랜덤 {i+1}", rand_grid(n, rng.choice([0.2, 0.5, 0.8]), [1, 1, 1, 2, 2, 3, 4, 5, 6]))
    case("최대 N 랜덤", rand_grid(20, 0.5, [1, 2, 3, 4, 5, 6]))
    case("최대 N 작은 물고기 위주", rand_grid(20, 0.7, [1, 1, 1, 2, 2, 3, 4, 5, 6]))
    g = [[rng.choice([1, 2, 3, 4, 5, 6]) for _ in range(20)] for _ in range(20)]
    g[19][19] = 9
    case("최대 N 꽉 찬 공간", g)
    # 크기 순서대로 먹으며 계속 자라도록 거리가 먼 곳에 흩뿌림
    g = [[0] * 20 for _ in range(20)]
    for r in range(20):
        for c in range(20):
            if (r + c) % 2 == 0:
                g[r][c] = min(6, 1 + (r * 20 + c) // 60)
    g[0][1] = 9
    case("최대 N 점점 자라는 상어", g)
    return cases
