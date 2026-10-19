def generate(rng):
    cases = []

    def case(name, k, grid, s, x, y):
        lines = [f"{len(grid)} {k}"] + [" ".join(map(str, r)) for r in grid] + [f"{s} {x} {y}"]
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    def rand_grid(n, k, p):
        return [[rng.randint(1, k) if rng.random() < p else 0 for _ in range(n)] for _ in range(n)]

    case("N=1 바이러스 있음", 1, [[1]], 0, 1, 1)
    case("N=1 바이러스 없음", 5, [[0]], 10000, 1, 1)
    case("바이러스가 하나도 없음", 3, [[0] * 4 for _ in range(4)], 10000, 2, 3)
    case("S=0 빈칸 조회", 2, [[1, 0], [0, 2]], 0, 1, 2)
    case("동시에 도착하면 작은 번호", 9, [[9, 0, 0, 0, 1]], 2, 1, 3)
    case("아직 도착 못 함", 3, [[3, 0, 0, 0, 0]], 3, 1, 5)
    case("정확히 S초에 도착", 3, [[3, 0, 0, 0, 0]], 4, 1, 5)
    for i in range(6):
        n = rng.randint(2, 15)
        k = rng.randint(1, 10)
        case(f"작은 랜덤 {i+1}", k, rand_grid(n, k, rng.choice([0.05, 0.1, 0.3])), rng.randint(0, 2 * n), rng.randint(1, n), rng.randint(1, n))
    N = 200
    g = [[0] * N for _ in range(N)]
    g[0][0] = 7
    case("최대 N 모서리 바이러스 1개", 7, g, 10000, N, N)
    g = [[0] * N for _ in range(N)]
    g[0][0] = 1000
    g[N - 1][N - 1] = 1
    case("최대 N 두 바이러스 경쟁", 1000, g, 10000, 1, N)
    g = rand_grid(N, 1000, 0.002)
    case("최대 N 희소 랜덤 K=1000", 1000, g, 10000, rng.randint(1, N), rng.randint(1, N))
    g = rand_grid(N, 1000, 0.3)
    case("최대 N 밀집 랜덤", 1000, g, 3, rng.randint(1, N), rng.randint(1, N))
    g = [[0] * N for _ in range(N)]
    g[N // 2][N // 2] = 2
    case("최대 N 중앙 바이러스 S 부족", 2, g, 150, 1, 1)
    # 서로 다른 종류 1000개를 위쪽 5줄에 몰아 두면 아래 끝까지 약 195초가 걸린다.
    # 매 초 종류마다 시험관 전체를 훑는 시뮬레이션은 O(S * K * N^2)로 시간 초과.
    perm = list(range(1, 1001))
    rng.shuffle(perm)
    g = [perm[r * N:(r + 1) * N] for r in range(5)] + [[0] * N for _ in range(N - 5)]
    case("최대 N 위쪽 5줄에 바이러스 1000종", 1000, g, 10000, N, rng.randint(1, N))
    g = [[0] * N for _ in range(N)]
    cells = rng.sample(range(N * N), 1000)
    for t, c in enumerate(cells, 1):
        g[c // N][c % N] = t
    case("최대 N 바이러스 1000종 흩어짐", 1000, g, 10000, rng.randint(1, N), rng.randint(1, N))
    return cases
