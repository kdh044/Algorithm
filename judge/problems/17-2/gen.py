def generate(rng):
    cases = []

    def case(name, n, pairs):
        lines = [f"{n} {len(pairs)}"] + [f"{a} {b}" for a, b in pairs]
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    def make(n, m, local=None):
        # 성적이 낮은 순서의 순열 order를 정하고, 그와 모순되지 않는 비교 결과 m개(중복 없음)를 만든다
        order = list(range(1, n + 1))
        rng.shuffle(order)
        pos = {v: i for i, v in enumerate(order)}
        seen = set()
        pairs = []
        while len(pairs) < m:
            if local:
                i = rng.randint(0, n - 2)
                j = min(n - 1, i + rng.randint(1, local))
            else:
                i, j = sorted(rng.sample(range(n), 2))
            a, b = order[i], order[j]
            if (a, b) in seen:
                continue
            seen.add((a, b))
            pairs.append((a, b))
        rng.shuffle(pairs)
        return pairs

    case("N=2 같은 비교 두 번", 2, [(2, 1), (2, 1)])
    case("N=3 모두 확정", 3, [(3, 1), (1, 2)])
    case("N=3 한 명만 확정", 3, [(1, 2), (1, 3)])
    case("답이 0", 4, [(1, 2), (3, 4)])
    case("N=4 일자 사슬 전원 확정", 4, [(4, 3), (3, 2), (2, 1)])
    case("두 덩어리로 분리", 6, [(1, 2), (2, 3), (4, 5), (5, 6)])
    case("별 모양", 5, [(1, 3), (2, 3), (3, 4), (3, 5)])
    for i in range(6):
        n = rng.randint(3, 15)
        mx = n * (n - 1) // 2
        case(f"작은 랜덤 {i+1}", n, make(n, rng.randint(2, mx)))
    n = 500
    order = list(range(1, n + 1))
    rng.shuffle(order)
    chain = [(order[i], order[i + 1]) for i in range(n - 1)]
    extra = []
    seen = set(chain)
    while len(chain) + len(extra) < 10000:
        i, j = sorted(rng.sample(range(n), 2))
        p = (order[i], order[j])
        if p not in seen:
            seen.add(p)
            extra.append(p)
    allp = chain + extra
    rng.shuffle(allp)
    case("최대 N, M 전원 확정(사슬 포함)", n, allp)
    case("최대 N, M 랜덤", 500, make(500, 10000))
    case("최대 N, M 가까운 순위끼리 비교", 500, make(500, 10000, local=40))
    case("최대 N, 최소 M", 500, make(500, 2))
    return cases
