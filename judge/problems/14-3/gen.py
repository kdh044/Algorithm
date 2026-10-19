def generate(rng):
    cases = []

    def case(name, n, stages):
        assert 1 <= n <= 500 and 1 <= len(stages) <= 200000 and all(1 <= s <= n + 1 for s in stages)
        cases.append({"name": name, "args": [n, stages]})

    case("N=1, 1명 실패", 1, [1])
    case("N=1, 1명 클리어", 1, [2])
    case("모두 클리어", 4, [5, 5, 5])
    case("모두 1단계", 4, [1, 1, 1])
    case("도달 못한 스테이지", 6, [1, 2, 2])
    case("실패율 동률(1/2 = 2/4)", 3, [1, 1, 2, 2, 4, 4, 3, 4])
    case("전부 실패율 1", 3, [1])
    for i in range(6):
        n = rng.randint(1, 10)
        case(f"작은 랜덤 {i+1}", n, [rng.randint(1, n + 1) for _ in range(rng.randint(1, 20))])
    m = 200000
    case("최대 랜덤", 500, [rng.randint(1, 501) for _ in range(m)])
    case("최대 전부 클리어", 500, [501] * m)
    case("최대 앞쪽 몰림", 500, [rng.randint(1, 20) for _ in range(m)])
    case("최대 뒤쪽 몰림", 500, [rng.randint(480, 501) for _ in range(m)])
    return cases
