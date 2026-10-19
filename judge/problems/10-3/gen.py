def generate(rng):
    cases = []

    def case(name, times, pres):
        n = len(times)
        assert 1 <= n <= 500 and all(1 <= t <= 100000 for t in times)
        lines = []
        for t, ps in zip(times, pres):
            assert len(set(ps)) == len(ps)
            lines.append(" ".join(map(str, [t] + list(ps) + [-1])))
        cases.append({"name": name, "input": f"{n}\n" + "\n".join(lines) + "\n"})

    def dag(n, p, tmax=100000, perm=True):
        # 위상 순서 order[0..n-1]을 정하고, 앞쪽 강의만 선수 강의로 삼는다
        order = list(range(1, n + 1))
        if perm:
            rng.shuffle(order)
        pres = {}
        for idx, v in enumerate(order):
            if p >= 1:
                ps = order[:idx]
            else:
                ps = [u for u in order[:idx] if rng.random() < p]
            ps = ps[:]
            rng.shuffle(ps)
            pres[v] = ps
        times = [rng.randint(1, tmax) for _ in range(n)]
        return times, [pres[v] for v in range(1, n + 1)]

    case("최소 N=1", [10], [[]])
    case("선수 강의 없음", [5, 3, 8], [[], [], []])
    case("번호가 큰 강의가 선수 강의", [1, 2, 3], [[2], [3], []])
    case("일직선", [100000] * 5, [[], [1], [2], [3], [4]])
    case("긴 경로 vs 짧은 경로", [1, 1, 1, 1, 50], [[], [1], [2], [3], [1, 4]])
    for i in range(6):
        n = rng.randint(2, 10)
        case(f"작은 랜덤 {i+1}", *dag(n, 0.4, 50))
    case("중간 랜덤", *dag(100, 0.1))
    # 최대 크기
    case("최대 N, 앞의 모든 강의가 선수 강의", *dag(500, 1))
    case("최대 N, 조밀한 랜덤 DAG", *dag(500, 0.5))
    case("최대 N, 희소한 랜덤 DAG", *dag(500, 0.01))
    times = [rng.randint(1, 100000) for _ in range(500)]
    case("최대 N 일직선 (역순 번호)", times, [[i + 2] if i < 499 else [] for i in range(500)])
    return cases
