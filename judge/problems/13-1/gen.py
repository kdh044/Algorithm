from collections import deque


def bfs(n, edges, x):
    g = [[] for _ in range(n + 1)]
    for a, b in edges:
        g[a].append(b)
    d = [-1] * (n + 1)
    d[x] = 0
    q = deque([x])
    while q:
        u = q.popleft()
        for v in g[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                q.append(v)
    return d


def best_k(n, edges, x):
    # 도달 가능한 거리 중 해당 도시가 가장 많은 K
    d = bfs(n, edges, x)
    cnt = {}
    for v in d[1:]:
        if v > 0:
            cnt[v] = cnt.get(v, 0) + 1
    if not cnt:
        return 1
    return max(cnt, key=lambda t: cnt[t])


def rand_edge(rng, lo, hi):
    a = rng.randint(lo, hi)
    b = rng.randint(lo, hi - 1)
    if b >= a:
        b += 1
    return a, b


def generate(rng):
    cases = []

    def case(name, n, k, x, edges):
        lines = [f"{n} {len(edges)} {k} {x}"]
        lines += [f"{a} {b}" for a, b in edges]
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    case("최소 N=2 K=1", 2, 1, 1, [(1, 2)])
    case("출발 도시로 들어오기만 함", 2, 1, 2, [(1, 2)])
    case("K가 너무 커서 -1", 5, 300000, 1, [(1, 2), (2, 3), (3, 4), (4, 5)])
    case("최단 거리가 아닌 경로 무시", 5, 3, 1, [(1, 2), (2, 3), (3, 4), (1, 4), (4, 5)])
    case("사이클", 4, 2, 3, [(1, 2), (2, 3), (3, 4), (4, 1)])
    case("중복 도로", 3, 1, 1, [(1, 2), (1, 2), (2, 3), (3, 1)])
    for i in range(6):
        n = rng.randint(2, 30)
        m = rng.randint(1, 60)
        edges = [rand_edge(rng, 1, n) for _ in range(m)]
        x = rng.randint(1, n)
        k = rng.randint(1, 5) if i % 2 else best_k(n, edges, x)
        case(f"작은 랜덤 {i+1}", n, k, x, edges)
    for i in range(2):
        n = rng.randint(1000, 3000)
        edges = [rand_edge(rng, 1, n) for _ in range(rng.randint(n, 3 * n))]
        x = rng.randint(1, n)
        case(f"중간 랜덤 {i+1}", n, best_k(n, edges, x), x, edges)

    N = 300000
    # 1) 최대 N 랜덤 그래프
    edges = [rand_edge(rng, 1, N) for _ in range(1000000)]
    x = rng.randint(1, N)
    case("최대 N 랜덤", N, best_k(N, edges, x), x, edges)

    # 2) 간선이 많은 경우: 번호가 작은 도시들끼리 촘촘히 연결 (나머지 도시는 고립)
    edges = [rand_edge(rng, 1, 1200) for _ in range(1000000)]
    case("최대 M 밀집", N, 2, 1, edges)

    # 3) 길이 N-1의 긴 경로 + 뒤로 가는 도로 (BFS 깊이 최대, 답은 N번 도시)
    edges = [(i, i + 1) for i in range(1, N)]
    for _ in range(1000000 - (N - 1)):
        a = rng.randint(2, N)
        b = rng.randint(max(1, a - 1000), a - 1)
        edges.append((a, b))
    rng.shuffle(edges)
    case("최대 깊이 경로", N, N - 1, 1, edges)

    # 4) 출발 도시에서 모든 도시로 바로 가는 별 모양 + 랜덤 도로 (답이 N-1개, 큐가 한 번에 커짐)
    x = rng.randint(1, N)
    edges = [(x, v) for v in range(1, N + 1) if v != x]
    edges += [rand_edge(rng, 1, N) for _ in range(1000000 - (N - 1))]
    rng.shuffle(edges)
    case("별 모양 K=1", N, 1, x, edges)
    return cases
