def generate(rng):
    cases = []

    def case(name, n, edges, x, k):
        assert 1 <= n <= 100 and 1 <= len(edges) <= 100 and 1 <= x <= n and 1 <= k <= n
        assert len(set(tuple(sorted(e)) for e in edges)) == len(edges) and all(a != b for a, b in edges)
        cases.append({"name": name, "input": f"{n} {len(edges)}\n" + "".join(f"{a} {b}\n" for a, b in edges) + f"{x} {k}\n"})

    def rand_edges(n, m, nodes=None):
        nodes = nodes or list(range(1, n + 1))
        allp = [(a, b) for i, a in enumerate(nodes) for b in nodes[i + 1:]]
        es = rng.sample(allp, m)
        return [(a, b) if rng.random() < 0.5 else (b, a) for a, b in es]

    case("N=2, X=K=2", 2, [(1, 2)], 2, 2)
    case("X=1, K=1 (제자리)", 3, [(1, 2), (2, 3)], 1, 1)
    case("K=1", 4, [(1, 2), (2, 3), (3, 4)], 4, 1)
    case("X=1 (돌아오기)", 4, [(1, 2), (2, 3), (3, 4)], 1, 4)
    case("K에 도달 불가", 4, [(1, 2), (3, 4)], 2, 3)
    case("K는 되지만 X 불가", 5, [(1, 2), (2, 3), (4, 5)], 4, 3)
    case("K가 N이 아님 (변수 덮어쓰기 버그 검출)", 6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)], 2, 3)
    path = [(i, i + 1) for i in range(1, 100)]
    case("최대 N 일직선, K=100, X=1", 100, path, 1, 100)
    case("최대 N 일직선, K=50, X=99", 100, path[:], 99, 50)
    for i in range(6):
        n = rng.randint(2, 10)
        m = rng.randint(1, n * (n - 1) // 2)
        case(f"작은 랜덤 {i+1}", n, rand_edges(n, m), rng.randint(1, n), rng.randint(1, n))
    for i in range(3):
        n = 100
        case(f"최대 N, M=100 랜덤 {i+1}", n, rand_edges(n, 100), rng.randint(1, n), rng.randint(1, n))
    # 조밀한 부분 그래프 (완전 그래프 14개 정점 = 91개 간선) -> 단순 경로 완전 탐색은 시간 초과
    nodes = list(range(1, 15))
    dense = rand_edges(14, 91, nodes)
    rest = [(i, i + 1) for i in range(14, 23)]
    case("완전 그래프 K14 + 꼬리", 100, dense + rest, 23, 14)
    nodes = rng.sample(range(1, 101), 14)
    if 1 not in nodes:
        nodes[0] = 1
    dense = rand_edges(100, 91, nodes)
    others = [v for v in range(1, 101) if v not in nodes]
    case("완전 그래프 K14 (흩어진 번호) + 고립 정점, X 불가", 100, dense + rand_edges(100, 9, others[:6]), others[0], nodes[5])
    case("완전 그래프 K14 (흩어진 번호), 도달 가능", 100, dense + [(nodes[3], others[1])] + rand_edges(100, 8, others[1:6]), others[2], nodes[7])
    return cases
