def generate(rng):
    cases = []

    def case(name, mat, plan):
        n = len(mat)
        lines = [f"{n} {len(plan)}"] + [" ".join(map(str, r)) for r in mat] + [" ".join(map(str, plan))]
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    def graph(n, comp, p):
        # comp[i]: 여행지 i(0-index)의 그룹. 같은 그룹 안에서만 확률 p로 도로, 그룹은 사슬로 연결 보장
        mat = [[0] * n for _ in range(n)]
        groups = {}
        for i in range(n):
            groups.setdefault(comp[i], []).append(i)
        for g in groups.values():
            order = g[:]
            rng.shuffle(order)
            for a, b in zip(order, order[1:]):
                mat[a][b] = mat[b][a] = 1
            for a in g:
                for b in g:
                    if a < b and rng.random() < p:
                        mat[a][b] = mat[b][a] = 1
        return mat, groups

    case("N=1, M=1", [[0]], [1])
    case("N=1 같은 곳 반복", [[0]], [1, 1, 1])
    case("N=2 연결 안 됨", [[0, 0], [0, 0]], [1, 2])
    case("N=2 연결", [[0, 1], [1, 0]], [2, 1, 2])
    case("M=1 고립된 여행지", [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [3])
    case("도로 없음, 같은 곳만 방문", [[0] * 4 for _ in range(4)], [3, 3])
    for i in range(8):
        n = rng.randint(2, 12)
        k = rng.randint(1, 3) if i % 2 == 0 else rng.randint(2, 4)
        comp = [rng.randint(0, k - 1) for _ in range(n)]
        mat, groups = graph(n, comp, rng.choice([0.0, 0.2, 0.5]))
        m = rng.randint(1, 10)
        if i % 2 == 0:
            g = groups[comp[rng.randint(0, n - 1)]]
            plan = [rng.choice(g) + 1 for _ in range(m)]
        else:
            plan = [rng.randint(1, n) for _ in range(m)]
        case(f"작은 랜덤 {i+1}", mat, plan)
    n = 500
    # 최대: 전부 연결(빽빽한 그래프), YES
    mat, groups = graph(n, [0] * n, 0.9)
    case("최대 N, M 빽빽한 그래프 YES", mat, [rng.randint(1, n) for _ in range(500)])
    # 최대: 두 그룹, 마지막에만 다른 그룹 -> NO
    comp = [rng.randint(0, 1) for _ in range(n)]
    mat, groups = graph(n, comp, 0.5)
    plan = [rng.choice(groups[0]) + 1 for _ in range(499)] + [rng.choice(groups[1]) + 1]
    case("최대 N, M 마지막 여행지만 불가 NO", mat, plan)
    # 최대: 긴 사슬 하나, 양 끝을 번갈아 방문 -> YES
    mat, groups = graph(n, [0] * n, 0.0)
    plan = [rng.randint(1, n) for _ in range(500)]
    case("최대 N, M 긴 사슬 YES", mat, plan)
    # 최대: 여러 그룹이지만 계획은 한 그룹 안 -> YES
    comp = [rng.randint(0, 4) for _ in range(n)]
    mat, groups = graph(n, comp, 0.6)
    case("최대 N, M 여러 그룹 중 한 그룹 YES", mat, [rng.choice(groups[2]) + 1 for _ in range(500)])
    # 최대: 고립된 여행지 하나가 계획 중간에 끼어 있음 -> NO
    comp = [0] * n
    comp[123] = 1
    mat, groups = graph(n, comp, 0.3)
    plan = [rng.choice(groups[0]) + 1 for _ in range(500)]
    plan[250] = 124
    case("최대 N, M 고립된 여행지가 중간에 NO", mat, plan)
    return cases
