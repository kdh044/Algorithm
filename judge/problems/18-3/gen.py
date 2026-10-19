def generate(rng):
    cases = []

    def case(name, n, edges):
        lines = [f"{n} {len(edges)}"] + [f"{x} {y} {z}" for x, y, z in edges]
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    def connected(n, m, zmax):
        perm = list(range(n))
        rng.shuffle(perm)
        es = []
        for i in range(1, n):
            es.append((perm[rng.randint(0, i - 1)], perm[i], rng.randint(1, zmax)))
        while len(es) < m:
            x, y = rng.sample(range(n), 2)
            es.append((x, y, rng.randint(1, zmax)))
        rng.shuffle(es)
        return es

    case("N=1, M=0", 1, [])
    case("N=2 도로 1개 (절약 0)", 2, [(0, 1, 5)])
    case("N=2 중복 도로", 2, [(0, 1, 5), (1, 0, 3), (0, 1, 9)])
    case("트리 (절약 0)", 5, [(0, 1, 4), (1, 2, 3), (1, 3, 2), (3, 4, 1)])
    case("모든 길이 같음", 4, [(0, 1, 7), (1, 2, 7), (2, 3, 7), (3, 0, 7), (0, 2, 7), (1, 3, 7)])
    for i in range(7):
        n = rng.randint(2, 15)
        m = rng.randint(n - 1, 30)
        case(f"작은 랜덤 {i+1}", n, connected(n, m, rng.choice([3, 100])))
    # 입력 조건의 최댓값은 N, M = 20만이지만, 저자 풀이(간선 튜플 정렬)가 이 채점기의 PyPy에서 0.9~1초(제한 1초)로
    # 아슬아슬해서 큰 케이스는 N = 10만으로 둔다(15만도 0.8~0.86초). O(N^2) 프림은 여전히 시간 초과.
    N = 100000
    case("큰 N, M 랜덤", N, connected(N, N, 10000))
    case("큰 N 트리 (M = N - 1)", N, connected(N, N - 1, 10000))
    # 번호가 큰 쪽 도로부터 처리되도록 비용을 배치: 재귀 find의 깊이가 매우 커지는 경우
    es = [(i, i + 1, (N - i) // 20 + 1) for i in range(N - 1)] + [(N - 1, 0, 10001)]
    rng.shuffle(es)
    case("큰 N 깊은 사슬", N, es)
    case("큰 N, M 작은 비용 다수 동률", N, connected(N, N, 3))
    return cases
