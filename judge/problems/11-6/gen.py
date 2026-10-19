def generate(rng):
    cases = []

    def case(name, ft, k):
        assert 1 <= len(ft) <= 200000 and all(1 <= x <= 100_000_000 for x in ft) and 1 <= k <= 2 * 10**13
        cases.append({"name": name, "args": [ft, k]})

    # 정확성
    case("음식 1개, 남음", [5], 3)
    case("음식 1개, 딱 다 먹음", [5], 5)
    case("다 먹고 남는 시간", [1, 1, 1], 10)
    case("합 - 1", [3, 1, 2], 5)
    case("합과 같음", [3, 1, 2], 6)
    case("k=1", [1, 1], 1)
    case("전부 같은 시간", [4] * 5, 13)
    case("한 바퀴 직후", [2, 3, 4], 3)
    for i in range(6):
        n = rng.randint(1, 30)
        ft = [rng.randint(1, 20) for _ in range(n)]
        k = rng.randint(1, sum(ft) + 2)
        case(f"작은 랜덤 {i+1}", ft, k)
    ft = [rng.randint(1, 1000) for _ in range(2000)]
    case("정확성 최대", ft, min(2_000_000, sum(ft) - 1))
    # 효율성
    n = 200000
    ft = [rng.randint(1, 100_000_000) for _ in range(n)]
    case("효율성 랜덤 합-1 근처", ft, min(2 * 10**13, sum(ft) - rng.randint(1, 1000)))
    ft = [rng.randint(1, 100_000_000) for _ in range(n)]
    case("효율성 랜덤 중간", ft, sum(ft) // 2)
    ft = list(range(1, n + 1))
    rng.shuffle(ft)
    case("효율성 서로 다른 값", ft, sum(ft) - 7)
    case("효율성 전부 최대", [100_000_000] * n, 2 * 10**13 - 1)
    ft = [rng.randint(1, 100_000_000) for _ in range(n)]
    case("효율성 -1", ft, 2 * 10**13)
    return cases
