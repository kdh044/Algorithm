def generate(rng):
    cases = []

    def case(name, grids):
        lines = [str(len(grids))]
        for g in grids:
            lines.append(str(len(g)))
            lines += [" ".join(map(str, r)) for r in g]
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    def rand_grid(n, lo=0, hi=9):
        return [[rng.randint(lo, hi) for _ in range(n)] for _ in range(n)]

    def snake(n):
        # 9로 된 벽 사이에 0으로 된 구불구불한 길: 최단 경로가 길게 돌아가야 함
        g = [[0] * n for _ in range(n)]
        for r in range(1, n, 2):
            for c in range(n):
                g[r][c] = 9
            if (r // 2) % 2 == 0:
                g[r][n - 1] = 0
            else:
                g[r][0] = 0
        return g

    case("N=2 최소", [[[1, 2], [3, 4]]])
    case("전부 0", [[[0] * 5 for _ in range(5)]])
    case("전부 9", [[[9] * 6 for _ in range(6)]])
    case("시작과 끝만 비용", [[[7, 0, 0], [0, 0, 0], [0, 0, 5]]])
    case("돌아가는 길이 유리", [snake(7)])
    for i in range(6):
        t = rng.randint(1, 4)
        case(f"작은 랜덤 {i+1}", [rand_grid(rng.randint(2, 12)) for _ in range(t)])
    case("최대 T, N 랜덤", [rand_grid(125) for _ in range(10)])
    case("최대 T, N 구불구불한 길", [snake(125) for _ in range(10)])
    case("최대 T, N 0과 9만", [[[rng.choice((0, 9)) for _ in range(125)] for _ in range(125)] for _ in range(10)])
    case("최대 T, N 작은 비용", [rand_grid(125, 0, 2) for _ in range(10)])
    return cases
