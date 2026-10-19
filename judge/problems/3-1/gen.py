def generate(rng):
    cases = []
    def case(name, n, m, k, arr):
        assert len(arr) == n and 1 <= k <= m
        cases.append({"name": name, "input": f"{n} {m} {k}\n{' '.join(map(str, arr))}\n"})
    case("책 예시 2 (같은 값 번갈아)", 5, 7, 2, [3, 4, 3, 4, 3])
    case("최소 N=2, M=1", 2, 1, 1, [1, 2])
    case("K=M", 3, 10, 10, [5, 1, 9])
    case("K=1 번갈아", 4, 9, 1, [7, 3, 8, 2])
    case("전부 같은 값", 6, 100, 3, [5] * 6)
    case("가장 큰 수 두 개", 5, 50, 4, [1, 10, 2, 10, 3])
    case("M이 K+1의 배수", 3, 12, 3, [1, 2, 3])
    case("M이 K+1의 배수 아님", 3, 13, 3, [1, 2, 3])
    for i in range(6):
        n = rng.randint(2, 20)
        m = rng.randint(1, 100)
        k = rng.randint(1, m)
        case(f"작은 랜덤 {i+1}", n, m, k, [rng.randint(1, 30) for _ in range(n)])
    n = 1000
    case("최대 N, M, K=M", n, 10000, 10000, [rng.randint(1, 10000) for _ in range(n)])
    case("최대 값 모두 10000, K=1", n, 10000, 1, [10000] * n)
    case("최대 랜덤", n, 10000, rng.randint(1, 10000), [rng.randint(1, 10000) for _ in range(n)])
    case("최대 랜덤 큰 수 1개", n, 10000, 7, [rng.randint(1, 9998) for _ in range(n - 1)] + [10000])
    return cases
