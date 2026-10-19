def generate(rng):
    cases = []
    def case(name, n, k):
        assert 2 <= k <= n <= 100000
        cases.append({"name": name, "input": f"{n} {k}\n"})
    case("최소 N=K=2", 2, 2)
    case("책 예시 17 4", 17, 4)
    case("책 예시 25 3", 25, 3)
    case("N=K", 99991, 99991)
    case("K의 거듭제곱", 3 ** 10, 3)
    case("2의 거듭제곱", 65536, 2)
    case("K-1 나머지", 26, 3)
    case("N이 K보다 1 큼", 100000, 99999)
    for i in range(7):
        k = rng.randint(2, 50)
        case(f"작은 랜덤 {i+1}", rng.randint(k, 1000), k)
    case("최대 N, K=2", 100000, 2)
    case("최대 N, K=100000", 100000, 100000)
    case("최대 N, 큰 K", 99999, 50000)
    case("최대 랜덤", 100000, rng.randint(2, 1000))
    case("빼기 많이", 99999, 316)
    return cases
