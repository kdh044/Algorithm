def generate(rng):
    cases = []
    def case(name, g):
        cases.append({"name": name, "input": f"{len(g)} {len(g[0])}\n" + "".join(" ".join(map(str, r)) + "\n" for r in g)})
    case("1x1", [[7]])
    case("한 행", [[5, 3, 9, 4]])
    case("한 열", [[5], [3], [9], [4]])
    case("전부 1", [[1] * 5 for _ in range(4)])
    case("전부 10000", [[10000] * 3 for _ in range(3)])
    case("행 최댓값이 함정", [[1, 10000, 10000], [5, 5, 5], [10000, 2, 10000]])
    case("마지막 행이 정답", [[3, 1], [2, 4], [9, 8]])
    for i in range(8):
        n, m = rng.randint(1, 10), rng.randint(1, 10)
        case(f"작은 랜덤 {i+1}", [[rng.randint(1, 20) for _ in range(m)] for _ in range(n)])
    case("최대 랜덤", [[rng.randint(1, 10000) for _ in range(100)] for _ in range(100)])
    case("최대 큰 값 위주", [[rng.randint(9000, 10000) for _ in range(100)] for _ in range(100)])
    g = [[rng.randint(1, 10000) for _ in range(100)] for _ in range(100)]
    for r in g:
        r[rng.randrange(100)] = 1
    g[rng.randrange(100)] = [rng.randint(5000, 10000) for _ in range(100)]
    case("최대 한 행만 큰 최솟값", g)
    return cases
