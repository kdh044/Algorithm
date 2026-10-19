# 입력 조건의 최댓값은 N = 10만, M = 100만이지만, 저자 풀이(간선 튜플 100만 개를 sort)가 PyPy에서
# M = 100만이면 약 6~7초 걸린다(PyPy의 튜플 정렬이 느림). 의도된 O(M log M) 풀이가 통과하도록
# 큰 케이스의 M은 30만으로 둔다. N = 10만은 그대로라 O(N^2) 풀이는 여전히 시간 초과.
BIGM = 300000
BIGM_WIDE = 300000


def generate(rng):
    cases = []

    def case(name, n, edges):
        assert 2 <= n <= 100000 and 1 <= len(edges) <= 1000000
        assert all(1 <= a <= n and 1 <= b <= n and a != b and 1 <= c <= 1000 for a, b, c in edges)
        cases.append({"name": name, "input": f"{n} {len(edges)}\n" + "".join(f"{a} {b} {c}\n" for a, b, c in edges)})

    def connected(n, m, cmax=1000):
        perm = list(range(1, n + 1))
        rng.shuffle(perm)
        es = []
        for i in range(1, n):
            p = perm[rng.randint(max(0, i - 50), i - 1)] if rng.random() < 0.5 else perm[rng.randint(0, i - 1)]
            es.append((perm[i], p, rng.randint(1, cmax)))
        while len(es) < m:
            a, b = rng.randint(1, n), rng.randint(1, n)
            if a != b:
                es.append((a, b, rng.randint(1, cmax)))
        rng.shuffle(es)
        return es

    case("최소 N=2 M=1", 2, [(1, 2, 7)])
    case("N=2 여러 길", 2, [(1, 2, 7), (2, 1, 3), (1, 2, 1000)])
    case("N=3 삼각형", 3, [(1, 2, 1), (2, 3, 2), (3, 1, 3)])
    case("모든 유지비 동일", 5, [(1, 2, 5), (2, 3, 5), (3, 4, 5), (4, 5, 5), (1, 5, 5), (2, 4, 5)])
    case("일직선 (가장 비싼 길 하나 제거)", 6, [(1, 2, 1), (2, 3, 1000), (3, 4, 2), (4, 5, 3), (5, 6, 4)])
    for i in range(6):
        n = rng.randint(2, 12)
        case(f"작은 랜덤 {i+1}", n, connected(n, rng.randint(n - 1, 3 * n), 20))
    case("중간 랜덤", 2000, connected(2000, 10000))
    n = 100000
    case("최대 N, 큰 M 랜덤", n, connected(n, BIGM_WIDE))
    case("최대 N, 큰 M, 유지비 범위 작음", n, connected(n, BIGM, 3))
    case("최대 N, 트리 (M = N-1)", n, connected(n, n - 1))
    chain = [(i, i + 1, rng.randint(1, 999)) for i in range(1, n)]
    extra = []
    while len(extra) < BIGM - len(chain):
        a, b = rng.randint(1, n), rng.randint(1, n)
        if a != b:
            extra.append((a, b, 1000))
    es = chain + extra
    rng.shuffle(es)
    case("최대 N, 큰 M, 일직선 + 비싼 간선(1000) 다수", n, es)
    return cases
