# 한쪽으로 긴 트리(체인)의 깊이는 DEPTH로 제한한다. 책의 재귀 find(10-7)가 기본 재귀 한도(1000, PyPy는 실제 약 880)에
# 걸리지 않도록 하기 위함이다. 경로 압축 없는 풀이의 시간 초과는 아래 "합치기/확인 교대" 케이스가 담당한다.
DEPTH = 500


def generate(rng):
    cases = []

    def case(name, n, ops):
        assert 1 <= n <= 100000 and 1 <= len(ops) <= 100000
        assert all(o in (0, 1) and 1 <= a <= n and 1 <= b <= n for o, a, b in ops)
        assert any(o == 1 for o, a, b in ops)
        cases.append({"name": name, "input": f"{n} {len(ops)}\n" + "".join(f"{o} {a} {b}\n" for o, a, b in ops)})

    def rand_ops(n, m, p_union):
        return [(0 if rng.random() < p_union else 1, rng.randint(1, n), rng.randint(1, n)) for _ in range(m)]

    case("최소 N=1 M=1", 1, [(1, 1, 1)])
    case("합치기 없이 확인만", 5, [(1, 1, 2), (1, 3, 3), (1, 5, 4)])
    case("자기 자신과 합치기", 3, [(0, 2, 2), (1, 2, 3), (0, 3, 2), (1, 2, 3)])
    case("이미 같은 팀 다시 합치기", 4, [(0, 1, 2), (0, 2, 1), (0, 3, 4), (1, 1, 4), (0, 2, 3), (1, 1, 4), (0, 4, 1), (1, 4, 2)])
    case("모두 하나의 팀", 6, [(0, i, i + 1) for i in range(1, 6)] + [(1, 1, 6), (1, 6, 3)])
    for i in range(6):
        n = rng.randint(2, 15)
        case(f"작은 랜덤 {i+1}", n, rand_ops(n, rng.randint(1, 25), 0.5))
    case("중간 랜덤", 1000, rand_ops(1000, 3000, 0.4))
    n = 100000
    case("최대 N, M 랜덤", n, rand_ops(n, 100000, 0.5))
    case("최대 N, M 합치기 위주", n, rand_ops(n, 100000, 0.9))
    case("최대 N, M 작은 번호 범위", n, [(rng.randint(0, 1), rng.randint(1, 300), rng.randint(1, 300)) for _ in range(100000)])
    # 체인: union(i, i+1)을 큰 번호부터 하면 i+1 -> i 로 길게 이어진다
    top = DEPTH + 1
    chain = [(0, i, i + 1) for i in range(DEPTH, 0, -1)]
    qs = [(1, rng.randint(top - 20, top), rng.randint(1, n)) for _ in range(100000 - len(chain))]
    case("깊은 체인 + 깊은 노드 반복 확인", n, chain + qs)
    chain = [(0, i + 1, i) for i in range(DEPTH, 0, -1)]
    qs = [(1, top, rng.randint(1, top)) if rng.random() < 0.9 else (0, rng.randint(top + 1, n), rng.randint(top + 1, n)) for _ in range(100000 - len(chain))]
    case("깊은 체인(인자 순서 반대) + 확인/합치기 혼합", n, chain + qs)
    # 합치기와 확인을 번갈아 하며 체인을 50,000까지 늘린다. 경로 압축이 있으면 매번 깊이 2 이하라
    # 재귀 find도 문제없지만, 경로 압축이 없으면 확인마다 체인 전체를 따라가 O(N^2)이 된다.
    L = 50000
    ops = []
    for i in range(L, 0, -1):
        ops.append((0, i, i + 1))
        ops.append((1, L + 1, rng.choice((i, i + 1, rng.randint(L + 2, n)))))
    case("합치기/확인 교대로 체인 50,000", n, ops)
    ops = []
    for i in range(L - 1000, 0, -1):
        ops.append((0, i + 1, i))
        ops.append((1, rng.choice((i, rng.randint(L + 2, n))), L - 999))
    while len(ops) < 100000:
        ops.append((0, rng.randint(L + 2, n), rng.randint(L + 2, n)))
    case("합치기/확인 교대로 체인(인자 순서 반대) + 기타 합치기", n, ops)
    return cases
