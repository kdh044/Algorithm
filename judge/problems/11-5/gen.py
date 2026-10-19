def generate(rng):
    cases = []

    def case(name, m, arr):
        assert 1 <= len(arr) <= 1000 and 1 <= m <= 10 and all(1 <= x <= m for x in arr)
        cases.append({"name": name, "input": f"{len(arr)} {m}\n{' '.join(map(str, arr))}\n"})

    case("최소 N=1", 1, [1])
    case("N=2 같은 무게", 3, [2, 2])
    case("N=2 다른 무게", 2, [1, 2])
    case("M=1 전부 같음", 1, [1] * 10)
    case("무게 M 사용 안 함", 10, [1, 2, 3])
    case("모두 다른 무게", 10, list(range(10, 0, -1)))
    for i in range(6):
        m = rng.randint(1, 10)
        n = rng.randint(1, 20)
        case(f"작은 랜덤 {i+1}", m, [rng.randint(1, m) for _ in range(n)])
    n = 1000
    case("최대 N 랜덤", 10, [rng.randint(1, 10) for _ in range(n)])
    case("최대 N 균등", 10, [i % 10 + 1 for i in range(n)])
    case("최대 N 전부 같음", 10, [7] * n)
    case("최대 N M=2", 2, [rng.randint(1, 2) for _ in range(n)])
    case("최대 N 한쪽 치우침", 10, [1] * 900 + [rng.randint(2, 10) for _ in range(100)])
    return cases
