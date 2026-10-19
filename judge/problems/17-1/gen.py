def generate(rng):
    cases = []

    def case(name, n, edges):
        lines = [str(n), str(len(edges))] + [f"{a} {b} {c}" for a, b, c in edges]
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    def rand_edges(n, m, cmax):
        es = []
        for _ in range(m):
            a = rng.randint(1, n)
            b = rng.randint(1, n - 1)
            if b >= a:
                b += 1
            es.append((a, b, rng.randint(1, cmax)))
        return es

    case("n=2 간선 1개", 2, [(1, 2, 5)])
    case("n=2 양방향", 2, [(1, 2, 3), (2, 1, 7)])
    case("중복 노선(최소만 사용)", 3, [(1, 2, 10), (1, 2, 3), (1, 2, 8), (2, 3, 4), (2, 3, 1)])
    case("도달 불가 다수", 5, [(1, 2, 1), (3, 4, 2)])
    case("한 방향 사슬", 6, [(i, i + 1, i) for i in range(1, 6)])
    case("직접보다 우회가 싼 경우", 4, [(1, 4, 100), (1, 2, 1), (2, 3, 1), (3, 4, 1)])
    for i in range(6):
        n = rng.randint(2, 12)
        case(f"작은 랜덤 {i+1}", n, rand_edges(n, rng.randint(1, 30), rng.choice([5, 100, 100000])))
    # 최대 비용 사슬: 경로 비용이 큰 경우
    n = 100
    case("최대 n 역순 사슬 최대 비용", n, [(i + 1, i, 100000) for i in range(1, n)] + [(1, n, 100000)])
    case("최대 n, m 랜덤", 100, rand_edges(100, 100000, 100000))
    case("최대 n, m 작은 비용", 100, rand_edges(100, 100000, 10))
    es = rand_edges(100, 99000, 100000)
    es += [(i, i % 100 + 1, 1) for i in range(1, 101)] * 10
    case("최대 n, m 원형 저비용 경로 포함", 100, es)
    return cases
