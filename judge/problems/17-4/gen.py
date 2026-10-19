def generate(rng):
    cases = []

    def case(name, n, edges):
        lines = [f"{n} {len(edges)}"] + [f"{a} {b}" for a, b in edges]
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    def connected(n, m, deep=False):
        # 무작위 트리(또는 깊은 트리) + 중복 없는 추가 간선, 번호는 무작위로 섞되 1번은 출발점
        perm = list(range(2, n + 1))
        rng.shuffle(perm)
        perm = [1] + perm
        es = set()
        for i in range(1, n):
            p = i - 1 if deep and rng.random() < 0.9 else rng.randint(max(0, i - 5) if deep else 0, i - 1)
            a, b = perm[p], perm[i]
            es.add((min(a, b), max(a, b)))
        while len(es) < m:
            a, b = rng.sample(range(1, n + 1), 2)
            es.add((min(a, b), max(a, b)))
        es = list(es)
        rng.shuffle(es)
        return [(a, b) if rng.random() < 0.5 else (b, a) for a, b in es]

    case("N=2", 2, [(1, 2)])
    case("N=2 역방향 표기", 2, [(2, 1)])
    case("별 모양(전부 거리 1)", 6, [(1, i) for i in range(2, 7)])
    case("일자 경로", 5, [(1, 2), (2, 3), (3, 4), (4, 5)])
    case("가장 먼 헛간이 번호가 작은 쪽", 5, [(5, 1), (5, 4), (4, 2), (4, 3)])
    case("사이클", 6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)])
    for i in range(6):
        n = rng.randint(2, 15)
        m = rng.randint(n - 1, min(n * (n - 1) // 2, 25))
        case(f"작은 랜덤 {i+1}", n, connected(n, m))
    n = 20000
    case("최대 N, M 랜덤", n, connected(n, 50000))
    case("최대 N 깊은 그래프", n, connected(n, 50000, deep=True))
    path = list(range(2, n + 1))
    rng.shuffle(path)
    path = [1] + path
    case("최대 N 일자 경로", n, [(path[i], path[i + 1]) for i in range(n - 1)])
    es = set()
    while len(es) < 50000 - (n - 1):
        a, b = rng.sample(range(2, n + 1), 2)
        es.add((min(a, b), max(a, b)))
    star = [(1, i) for i in range(2, n + 1)] + list(es)
    rng.shuffle(star)
    case("최대 N, M 별 모양 + 잎끼리 간선", n, star)
    return cases
