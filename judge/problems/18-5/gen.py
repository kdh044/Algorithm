def generate(rng):
    cases = []

    def fmt(tcs):
        lines = [str(len(tcs))]
        for old, pairs in tcs:
            lines.append(str(len(old)))
            lines.append(" ".join(map(str, old)))
            lines.append(str(len(pairs)))
            lines += [f"{a} {b}" for a, b in pairs]
        return "\n".join(lines) + "\n"

    def case(name, tcs):
        cases.append({"name": name, "input": fmt(tcs)})

    def changed_pairs(old, new):
        pos = {v: i for i, v in enumerate(new)}
        res = []
        n = len(old)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = old[i], old[j]
                if pos[a] > pos[b]:
                    res.append((min(a, b), max(a, b)))
        return res

    def perturb(old, k, seg):
        new = old[:]
        n = len(new)
        for _ in range(k):
            L = rng.randint(2, min(seg, n))
            s = rng.randint(0, n - L)
            if rng.random() < 0.5:
                new[s:s + L] = new[s:s + L][::-1]
            else:
                t = rng.randint(0, n - 1)
                new[s], new[t] = new[t], new[s]
        return new

    def consistent(n, k=None, seg=None, limit=25000):
        old = list(range(1, n + 1))
        rng.shuffle(old)
        if k is None:
            k = rng.randint(0, max(1, n // 3))
        if seg is None:
            seg = max(2, n // 4)
        while True:
            new = perturb(old, k, seg)
            pairs = changed_pairs(old, new)
            if len(pairs) <= limit:
                break
            k = max(1, k // 2)
        rng.shuffle(pairs)
        return old, pairs

    def broken(n, k=None, seg=None):
        # 일관된 정보에서 쌍을 하나 추가하거나 빼서 모순(사이클)이 생길 수 있게 만든다
        old, pairs = consistent(n, k, seg, limit=24999)
        s = set(pairs)
        if pairs and rng.random() < 0.5:
            pairs = pairs[:]
            pairs.pop(rng.randrange(len(pairs)))
        else:
            while True:
                a, b = sorted(rng.sample(range(1, n + 1), 2))
                if (a, b) not in s:
                    pairs = pairs + [(a, b)]
                    break
        rng.shuffle(pairs)
        return old, pairs

    # 기본/경계
    case("n=2 변화 없음", [([2, 1], [])])
    case("n=2 순위 교환", [([1, 2], [(1, 2)])])
    case("변화 없음 (m=0)", [([3, 1, 4, 2, 5], [])])
    case("완전히 뒤집힘", [([1, 2, 3, 4], [(a, b) for a in range(1, 5) for b in range(a + 1, 5)])])
    case("세 팀 사이클 IMPOSSIBLE", [([1, 2, 3], [(1, 3)])])
    case("IMPOSSIBLE 여러 개", [([1, 2, 3, 4], [(1, 3)]), ([4, 3, 2, 1], [(1, 3), (2, 4)]), ([2, 1, 3], [(2, 3)])])
    for i in range(6):
        tcs = []
        for _ in range(rng.randint(1, 8)):
            n = rng.randint(2, 10)
            tcs.append(consistent(n) if rng.random() < 0.5 else broken(n))
        case(f"작은 랜덤 {i+1}", tcs)
    case("T=100 작은 n 섞음", [consistent(rng.randint(2, 8)) if i % 2 else broken(rng.randint(3, 8)) for i in range(100)])
    # 큰 케이스
    case("n=500, m 최대에 가까운 일관된 정보", [consistent(500, 30, 120) for _ in range(8)])
    case("n=500 IMPOSSIBLE과 정상 섞음", [broken(500, 30, 120) if i % 2 else consistent(500, 30, 120) for i in range(8)])
    case("n=500 IMPOSSIBLE만", [broken(500, 40, 100) for _ in range(8)])
    case("T=100, n=50 섞음", [consistent(50) if i % 3 else broken(50) for i in range(100)])
    # T = 100, n = 500을 동시에 주면 저자 풀이(인접 행렬 O(T * n^2))가 이 채점기의 PyPy에서 약 1초(제한 1초)라 T = 50으로 둔다.
    case("T=50, n=500 섞음", [consistent(500, 8, 50) if i % 3 else broken(500, 8, 50) for i in range(50)])
    return cases
