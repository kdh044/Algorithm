LIM = 10 ** 9


def check(a, ops):
    # 모든 연산자 배치에서 중간 결과가 범위 안인지, 최종 최대/최소가 ±10억 경계값과 같지 않은지 확인
    res = []
    cnt = list(ops)

    def dfs(i, now):
        if abs(now) > LIM:
            return False
        if i == len(a):
            res.append(now)
            return True
        for t in range(4):
            if cnt[t]:
                cnt[t] -= 1
                if t == 0:
                    nv = now + a[i]
                elif t == 1:
                    nv = now - a[i]
                elif t == 2:
                    nv = now * a[i]
                else:
                    nv = abs(now) // a[i] * (1 if now >= 0 else -1)
                ok = dfs(i + 1, nv)
                cnt[t] += 1
                if not ok:
                    return False
        return True

    if not dfs(1, a[0]):
        return False
    return max(res) not in (LIM, -LIM) and min(res) not in (LIM, -LIM)


def generate(rng):
    cases = []

    def case(name, a, ops):
        assert check(a, ops) and sum(ops) == len(a) - 1
        cases.append({"name": name, "input": f"{len(a)}\n{' '.join(map(str, a))}\n{' '.join(map(str, ops))}\n"})

    def rand_ops(k):
        ops = [0, 0, 0, 0]
        for _ in range(k):
            ops[rng.randrange(4)] += 1
        return ops

    def rand_case(n, hi, ops=None):
        while True:
            a = [rng.randint(1, hi) for _ in range(n)]
            o = list(ops) if ops else rand_ops(n - 1)
            if check(a, o):
                return a, o

    case("N=2 덧셈", [1, 1], [1, 0, 0, 0])
    case("N=2 뺄셈", [1, 100], [0, 1, 0, 0])
    case("N=2 나눗셈 몫 0", [3, 100], [0, 0, 0, 1])
    case("음수 나눗셈", [1, 5, 3], [0, 1, 0, 1])
    case("곱셈만", [100, 100, 100, 100], [0, 0, 3, 0])
    case("나눗셈만", [100, 3, 2, 7, 1], [0, 0, 0, 4])
    case("모든 수가 같음", [7] * 11, [3, 3, 2, 2])
    for i in range(6):
        n = rng.randint(3, 8)
        case(f"작은 랜덤 {i+1}", *rand_case(n, 100))
    # N=11에서 경우의 수가 가장 많은 연산자 배분 (10! / (3!3!2!2!) = 25,200가지)
    for i, ops in enumerate([[3, 3, 2, 2], [2, 3, 3, 2], [3, 2, 2, 3], [2, 2, 3, 3]]):
        case(f"최대 N 연산자 고르게 {i+1}", *rand_case(11, 100 if ops[2] <= 2 else 30, ops))
    case("최대 N 큰 곱", *rand_case(11, 100, [2, 2, 4, 2]))
    case("최대 N 랜덤", *rand_case(11, 100))
    return cases
