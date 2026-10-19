def generate(rng):
    cases = []

    def case(name, tcs):
        s = [str(len(tcs))]
        for n, m, g in tcs:
            s.append(f"{n} {m}")
            s.append(" ".join(map(str, g)))
        cases.append({"name": name, "input": "\n".join(s) + "\n"})

    def rand_tc(n, m, lo=1, hi=100):
        return (n, m, [rng.randint(lo, hi) for _ in range(n * m)])

    case("1x1", [(1, 1, [7])])
    case("한 행", [(1, 5, [1, 2, 3, 4, 5])])
    case("한 열", [(5, 1, [3, 9, 1, 2, 4])])
    case("2행 지그재그", [(2, 4, [1, 100, 1, 100, 100, 1, 100, 1])])
    case("전부 100", [(20, 20, [100] * 400)])
    case("여러 테스트 작은", [rand_tc(rng.randint(1, 4), rng.randint(1, 4)) for _ in range(10)])
    for i in range(5):
        case(f"작은 랜덤 {i+1}", [rand_tc(rng.randint(1, 8), rng.randint(1, 8)) for _ in range(rng.randint(1, 5))])
    case("20x20 한 개", [rand_tc(20, 20)])
    case("최대 T=1000, 20x20 랜덤", [rand_tc(20, 20) for _ in range(1000)])
    case("최대 T=1000, 20x20 전부 1", [(20, 20, [1] * 400) for _ in range(1000)])
    case("최대 T=1000, 크기 혼합", [rand_tc(rng.randint(1, 20), rng.randint(1, 20)) for _ in range(1000)])
    return cases
