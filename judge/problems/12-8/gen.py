def generate(rng):
    cases = []
    def case(name, n, weak, dist):
        assert 1 <= n <= 200 and 1 <= len(weak) <= 15 and 1 <= len(dist) <= 8
        assert weak == sorted(set(weak)) and all(0 <= w <= n - 1 for w in weak)
        assert all(1 <= d <= 100 for d in dist)
        cases.append({"name": name, "args": [n, weak, dist]})

    def rw(n, k):
        return sorted(rng.sample(range(n), k))

    def rd(k, lo=1, hi=100):
        return [rng.randint(lo, hi) for _ in range(k)]

    case("최소 n=1", 1, [0], [1])
    case("취약 지점 1개", 200, [137], [1])
    case("0과 n-1이 붙어 있음(원형)", 200, [0, 199], [1])
    case("친구 1명으로 불가 -> -1", 10, [0, 5], [1])
    case("모두 투입해야 함", 16, [0, 2, 4, 6, 8, 10, 12, 14], [1, 1, 1, 1, 1, 1, 1, 1])
    case("한 명이 한 바퀴 거의 전부", 200, list(range(0, 200, 14)), [100, 1])
    for i in range(6):
        n = rng.randint(5, 50)
        k = rng.randint(1, min(n, 10))
        case(f"작은 랜덤 {i+1}", n, rw(n, k), rd(rng.randint(1, 5), 1, max(1, n // 3)))
    # 최대 크기 (weak 15, dist 8)
    n = 200
    even = [i * 13 for i in range(15)]
    case("최대: 균등 간격, 거리 작음(-1)", n, even, [1] * 8)
    case("최대: 균등 간격, 거리 12 (-1)", n, even, [12] * 8)
    case("최대: 8명 전부 필요", n, even, [13] * 8)
    case("최대: 7명 필요", n, even, [13, 13, 13, 13, 13, 13, 13, 26])
    case("최대: 8명 전부 필요, 이동 거리 큼", n, even, [25] * 8)
    case("최대: 한 명만 멀리 감", n, even, [12] * 7 + [100])
    case("최대: 서로 다른 거리 8명 전부 필요", n, even, [12, 14, 16, 18, 20, 22, 24, 25])
    case("최대: 랜덤 weak, 작은 dist", n, rw(n, 15), rd(8, 1, 10))
    case("최대: 랜덤 weak, 서로 다른 dist", n, rw(n, 15), rng.sample(range(5, 40), 8))
    case("최대: 랜덤 weak, 큰 dist", n, rw(n, 15), rd(8, 50, 100))
    case("최대: 촘촘한 weak", n, list(range(100, 115)), rd(8, 1, 3))
    return cases
