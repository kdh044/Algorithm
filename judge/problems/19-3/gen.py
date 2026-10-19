def generate(rng):
    cases = []

    def case(name, n, k, cells, dirs, prios):
        # cells: 상어 번호 순서대로 (r, c)
        g = [[0] * n for _ in range(n)]
        for i, (r, c) in enumerate(cells):
            g[r][c] = i + 1
        lines = [f"{n} {len(cells)} {k}"] + [" ".join(map(str, row)) for row in g]
        lines.append(" ".join(map(str, dirs)))
        for p in prios:
            for row in p:
                lines.append(" ".join(map(str, row)))
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    def valid(n, cells):
        occ = set(cells)
        for r, c in cells:
            if not any(0 <= r + dr < n and 0 <= c + dc < n and (r + dr, c + dc) not in occ
                       for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                return False
        return True

    def rand_prio():
        res = []
        for _ in range(4):
            p = [1, 2, 3, 4]
            rng.shuffle(p)
            res.append(p)
        return res

    def rand_case(name, n, m, k, prio=None):
        allc = [(r, c) for r in range(n) for c in range(n)]
        cells = rng.sample(allc, m)
        # 인접한 빈칸이 없는 상어는 제거 (입력 조건 보장)
        while not valid(n, cells):
            occ = set(cells)
            cells = [(r, c) for r, c in cells
                     if any(0 <= r + dr < n and 0 <= c + dc < n and (r + dr, c + dc) not in occ
                            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))]
        m = len(cells)
        dirs = [rng.randint(1, 4) for _ in range(m)]
        prios = [prio() if prio else rand_prio() for _ in range(m)]
        case(name, n, k, cells, dirs, prios)


    def simulate(n, k, cells, dirs, prios):
        # 결과가 -1이 아닌 케이스를 고르기 위한 간단한 시뮬레이터
        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pos = {i + 1: rc for i, rc in enumerate(cells)}
        d = {i + 1: dirs[i] for i in range(len(cells))}
        smell = {}
        for s_, (r, c) in pos.items():
            smell[(r, c)] = (s_, k)
        for t in range(1, 1001):
            newpos = {}
            for s_ in sorted(pos):
                r, c = pos[s_]
                pr = prios[s_ - 1][d[s_] - 1]
                choice = None
                for want_own in (False, True):
                    for nd in pr:
                        nr, nc = r + D[nd - 1][0], c + D[nd - 1][1]
                        if 0 <= nr < n and 0 <= nc < n:
                            sm = smell.get((nr, nc))
                            if (not want_own and sm is None) or (want_own and sm is not None and sm[0] == s_):
                                choice = (nd, nr, nc)
                                break
                    if choice:
                        break
                nd, nr, nc = choice
                d[s_] = nd
                if (nr, nc) not in [newpos[x] for x in newpos]:
                    newpos[s_] = (nr, nc)
            pos = newpos
            smell = {key: (v[0], v[1] - 1) for key, v in smell.items() if v[1] > 1}
            for s_, rc in pos.items():
                smell[rc] = (s_, k)
            if len(pos) == 1:
                return t
        return -1

    def finishing(name, n, m, k, tries=3000):
        allc = [(r, c) for r in range(n) for c in range(n)]
        for _ in range(tries):
            cells = rng.sample(allc, m)
            if not valid(n, cells):
                continue
            dirs = [rng.randint(1, 4) for _ in range(m)]
            prios = [rand_prio() for _ in range(m)]
            if simulate(n, k, cells, dirs, prios) != -1:
                case(name, n, k, cells, dirs, prios)
                return
        raise RuntimeError("no finishing case: " + name)

    same = [[1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 2], [4, 3, 2, 1]]
    case("N=2 두 상어 바로 만남", 2, 1, [(0, 0), (0, 1)], [4, 3], [same, same])
    case("N=2 냄새 오래 지속", 2, 1000, [(0, 0), (1, 1)], [1, 1], [same, same])
    case("두 상어가 같은 방향으로만 맴돎", 3, 2, [(0, 0), (2, 2)], [4, 3],
         [[[4, 2, 3, 1]] * 4, [[3, 1, 4, 2]] * 4])
    case("모든 우선순위 동일", 4, 3, [(0, 0), (3, 3), (0, 3)], [2, 1, 3], [same, same, same])
    for i in range(8):
        n = rng.randint(2, 6)
        m = rng.randint(2, min(n * n - 1, 6))
        rand_case(f"작은 랜덤 {i+1}", n, m, rng.choice([1, 2, 3, 5, 10, 1000]))
    rand_case("최대 N, 상어 2마리, k=1", 20, 2, 1)
    rand_case("최대 N, 상어 2마리, k=1000", 20, 2, 1000)
    rand_case("최대 N, 상어 많음, k=1000", 20, 300, 1000)
    rand_case("최대 N, 상어 많음, k=1", 20, 300, 1)
    rand_case("최대 N, 상어 50마리, k=10", 20, 50, 10)
    rand_case("최대 N, 상어 10마리, k=50", 20, 10, 50)
    rand_case("최대 N, 상어 5마리, k=4", 20, 5, 4)
    for i, (n, m, k) in enumerate([(3, 2, 1), (4, 3, 2), (5, 5, 3), (6, 3, 2), (10, 4, 2), (15, 3, 3), (20, 3, 2), (20, 2, 5), (20, 4, 1)]):
        finishing(f"1번만 남는 경우 {i+1} (N={n}, M={m}, k={k})", n, m, k)
    return cases
