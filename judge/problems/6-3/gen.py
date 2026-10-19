def generate(rng):
    cases = []
    MX = 9999999

    def case(name, k, a, b):
        n = len(a)
        assert len(b) == n and 1 <= n <= 100000 and 0 <= k <= n
        assert all(1 <= x <= MX for x in a) and all(1 <= x <= MX for x in b)
        cases.append({"name": name, "input": f"{n} {k}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}\n"})

    case("N=1 K=0", 0, [1], [5])
    case("N=1 K=1 교체", 1, [1], [5])
    case("N=1 K=1 교체 안 함", 1, [5], [1])
    case("K=0", 0, [1, 2, 3], [9, 9, 9])
    case("A가 전부 큼", 3, [10, 20, 30], [1, 2, 3])
    case("같은 값은 교체 이득 없음", 2, [5, 5, 5], [5, 5, 5])
    case("일부만 이득", 4, [1, 2, 8, 9], [7, 3, 1, 1])
    for i in range(7):
        n = rng.randint(1, 20)
        case(f"작은 랜덤 {i+1}", rng.randint(0, n),
             [rng.randint(1, 30) for _ in range(n)], [rng.randint(1, 30) for _ in range(n)])
    N = 100000
    case("최대 K=N 전부 교체", N, [rng.randint(1, 5000000) for _ in range(N)],
         [rng.randint(5000001, MX) for _ in range(N)])
    case("최대 랜덤 K=N", N, [rng.randint(1, MX) for _ in range(N)], [rng.randint(1, MX) for _ in range(N)])
    case("최대 랜덤 K 절반", N // 2, [rng.randint(1, MX) for _ in range(N)], [rng.randint(1, MX) for _ in range(N)])
    case("최대 값 경계", N, [1] * N, [MX] * N)
    return cases
