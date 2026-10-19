from collections import deque

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]


def fmt(n, apples, turns):
    assert 2 <= n <= 100 and 0 <= len(apples) <= 100 and 1 <= len(turns) <= 100
    assert len(set(apples)) == len(apples) and (1, 1) not in apples
    assert all(1 <= a <= n and 1 <= b <= n for a, b in apples)
    xs = [x for x, _ in turns]
    assert all(1 <= x <= 10000 for x in xs) and all(xs[i] < xs[i + 1] for i in range(len(xs) - 1))
    lines = [str(n), str(len(apples))] + [f"{a} {b}" for a, b in apples]
    lines += [str(len(turns))] + [f"{x} {c}" for x, c in turns]
    return "\n".join(lines) + "\n"


def survive(rng, n, apples, max_turns, p_random):
    """뱀을 직접 움직여 보며, 다음 칸이 막히면 살 수 있는 쪽으로 회전하도록 회전 정보를 만든다."""
    apple = set(apples)
    body = deque([(1, 1)])
    occ = {(1, 1)}
    d = 0
    x = y = 1
    t = 0
    turns = []

    def free(nx, ny):
        return 1 <= nx <= n and 1 <= ny <= n and (nx, ny) not in occ

    while len(turns) < max_turns and t < 9990:
        # 이동
        nx, ny = x + DX[d], y + DY[d]
        if not free(nx, ny):
            break
        x, y = nx, ny
        body.append((x, y)); occ.add((x, y))
        if (x, y) in apple:
            apple.discard((x, y))
        else:
            occ.discard(body.popleft())
        t += 1
        # 회전 결정
        ahead = free(x + DX[d], y + DY[d])
        if not ahead or rng.random() < p_random:
            opts = []
            for c, nd in (("L", (d - 1) % 4), ("D", (d + 1) % 4)):
                if free(x + DX[nd], y + DY[nd]):
                    opts.append((c, nd))
            if opts:
                c, nd = rng.choice(opts)
                turns.append((t, c))
                d = nd
            elif not turns or turns[-1][0] != t:
                turns.append((t, rng.choice("LD")))
                break
    if not turns:
        turns.append((rng.randint(1, 10000), rng.choice("LD")))
    return turns


def rand_apples(rng, n, k):
    cells = [(a, b) for a in range(1, n + 1) for b in range(1, n + 1) if (a, b) != (1, 1)]
    return rng.sample(cells, min(k, len(cells)))


def rand_turns(rng, l, maxx):
    xs = sorted(rng.sample(range(1, maxx + 1), l))
    return [(x, rng.choice("LD")) for x in xs]


def generate(rng):
    cases = []
    def case(name, n, apples, turns):
        cases.append({"name": name, "input": fmt(n, apples, turns)})

    case("N=2 바로 벽", 2, [], [(10000, "D")])
    case("N=2 한 바퀴 돌고 몸에 부딪힘", 2, [(1, 2), (2, 2)], [(1, "D"), (2, "D"), (3, "D")])
    case("N=2 사과로 꽉 참", 2, [(1, 2), (2, 2), (2, 1)], [(1, "D"), (2, "D"), (3, "D")])
    case("회전 전에 벽", 5, [], [(100, "L")])
    case("왼쪽으로 돌아 바로 벽", 5, [], [(1, "L")])
    case("사과 연속으로 먹고 꺾어서 몸에 충돌", 10, [(1, c) for c in range(2, 8)], [(7, "D"), (8, "D"), (9, "D")])
    case("X=10000 회전(게임이 먼저 끝남)", 100, [], [(10000, "D")])
    for i in range(5):
        n = rng.randint(3, 12)
        apples = rand_apples(rng, n, rng.randint(0, min(100, n * n - 1)))
        turns = rand_turns(rng, rng.randint(1, 15), 40)
        case(f"작은 랜덤 {i+1}", n, apples, turns)
    for i in range(3):
        n = rng.randint(4, 15)
        apples = rand_apples(rng, n, rng.randint(0, min(100, n * n // 2)))
        case(f"작은 생존형 {i+1}", n, apples, survive(rng, n, apples, 100, 0.2))
    # 최대 크기
    n = 100
    # 사과 없이 지그재그(오래 생존)
    turns = []
    t = 0
    for r in range(50):
        t += 99
        turns.append((t, "D" if r % 2 == 0 else "L"))
        t += 1
        turns.append((t, "D" if r % 2 == 0 else "L"))
    case("최대 N, 지그재그 100번 회전", n, [], turns)
    apples = [(1, c) for c in range(2, 102) if c <= 100] + [(2, 100)]
    apples = apples[:100]
    case("최대 N, 사과 100개를 한 줄에 먹고 지그재그", n, apples, turns)
    apples = rand_apples(rng, n, 100)
    case("최대 N, 생존형 랜덤 사과 100개", n, apples, survive(rng, n, apples, 100, 0.03))
    apples = rand_apples(rng, n, 100)
    case("최대 N, 생존형 랜덤 사과 100개 2", n, apples, survive(rng, n, apples, 100, 0.01))
    case("최대 N, 완전 랜덤", n, rand_apples(rng, n, 100), rand_turns(rng, 100, 10000))
    return cases
