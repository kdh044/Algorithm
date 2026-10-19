def generate(rng):
    cases = []
    def case(name, arr):
        cases.append({"name": name, "input": f"{len(arr)}\n{' '.join(map(str, arr))}\n"})

    def build(n, k, lo, hi):
        # d[i] = a[i] - i 는 비감소. k가 고정점 위치(None이면 없음).
        # i<k: d<0, i==k: d=0, i>k: d>0  -> 고정점은 최대 1개
        if k is None:
            if rng.random() < 0.5:
                d = sorted(rng.randint(lo, -1) for _ in range(n))
            elif rng.random() < 0.5:
                d = sorted(rng.randint(1, hi) for _ in range(n))
            else:
                m = rng.randint(0, n)
                d = sorted(rng.randint(lo, -1) for _ in range(m)) + sorted(rng.randint(1, hi) for _ in range(n - m))
        else:
            d = sorted(rng.randint(lo, -1) for _ in range(k)) + [0] + sorted(rng.randint(1, hi) for _ in range(n - k - 1))
        return [i + x for i, x in enumerate(d)]

    case("N=1 고정점 0", [0])
    case("N=1 없음(음수)", [-1])
    case("N=1 없음(양수)", [5])
    case("고정점이 맨 뒤", [-10, -5, 0, 3])
    case("모두 인덱스보다 1 큼", [1, 2, 3, 4, 5])
    case("모두 인덱스보다 1 작음", [-1, 0, 1, 2, 3])
    case("극값", [-10**9, 1, 10**9])
    for i in range(6):
        n = rng.randint(1, 30)
        k = rng.choice([None, rng.randrange(n)])
        case(f"작은 랜덤 {i+1}", build(n, k, -5, 5))
    n = 10**6
    case("최대 N 고정점 중간", build(n, rng.randrange(n // 4, 3 * n // 4), -10**6, 10**6))
    case("최대 N 고정점 맨 앞", build(n, 0, -10**6, 10**6))
    case("최대 N 고정점 맨 뒤", build(n, n - 1, -10**6, 10**6))
    case("최대 N 고정점 없음", build(n, None, -10**6, 10**6))
    case("최대 N 연속(-1 차이)", [i - 1 for i in range(n)])
    return cases
