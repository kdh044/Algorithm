def generate(rng):
    cases = []

    def case(name, n, c, edges):
        assert 1 <= n <= 30000 and 1 <= len(edges) <= 200000 and 1 <= c <= n
        assert all(1 <= x <= n and 1 <= y <= n and x != y and 1 <= z <= 1000 for x, y, z in edges)
        cases.append({"name": name, "input": f"{n} {len(edges)} {c}\n" + "".join(f"{x} {y} {z}\n" for x, y, z in edges)})

    def rand_edge(n):
        x = rng.randint(1, n)
        y = rng.randint(1, n - 1)
        if y >= x:
            y += 1
        return (x, y, rng.randint(1, 1000))

    case("메시지를 받는 도시 없음", 2, 1, [(2, 1, 5)])
    case("N=2 한 통로", 2, 1, [(1, 2, 1000)])
    case("방향 확인 (역방향만 존재)", 3, 2, [(1, 2, 3), (3, 2, 1), (1, 3, 7)])
    case("더 먼 경로가 빠른 경우", 4, 1, [(1, 4, 100), (1, 2, 1), (2, 3, 1), (3, 4, 1)])
    case("중복 통로", 3, 1, [(1, 2, 9), (1, 2, 3), (2, 3, 5), (2, 3, 1)])
    case("일부만 도달", 6, 3, [(3, 1, 2), (1, 2, 2), (4, 5, 1), (5, 6, 1), (6, 3, 1)])
    for i in range(6):
        n = rng.randint(2, 12)
        m = rng.randint(1, 30)
        case(f"작은 랜덤 {i+1}", n, rng.randint(1, n), [rand_edge(n) for _ in range(m)])
    for i in range(2):
        n = rng.randint(500, 2000)
        case(f"중간 랜덤 {i+1}", n, rng.randint(1, n), [rand_edge(n) for _ in range(rng.randint(n, 5 * n))])
    n = 30000
    # 큰 케이스: N, M 모두 입력 조건 최댓값. N이 최대(30,000)라 O(N^2) 다익스트라는 시간 초과.
    BIGM = 200000
    case("최대 N, 큰 M 랜덤", n, rng.randint(1, n), [rand_edge(n) for _ in range(BIGM)])
    chain = [(i, i + 1, rng.randint(1, 1000)) for i in range(1, n)]
    case("최대 N 일직선 + 랜덤 간선", n, 1, chain + [rand_edge(n) for _ in range(BIGM - len(chain))])
    # 갱신이 많이 일어나도록: 시작점에서 모든 도시로 비싼 간선, 그리고 싼 간선 여러 개
    es = [(1, v, 1000) for v in range(2, n + 1)]
    es += [rand_edge(n)[:2] + (rng.randint(1, 30),) for _ in range(BIGM - len(es))]
    rng.shuffle(es)
    case("최대 N, 큰 M, 갱신이 많은 구조", n, 1, es)
    case("최대 N, 큰 M, 시작점에서 나가는 통로 없음", n, n, [(x if x != n else 1, y, z) if (x if x != n else 1) != y else (1, 2, z) for x, y, z in (rand_edge(n) for _ in range(BIGM))])
    return cases
