def generate(rng):
    cases = []

    def case(name, tri):
        cases.append({"name": name, "input": f"{len(tri)}\n" + "\n".join(" ".join(map(str, r)) for r in tri) + "\n"})

    def rand(n, lo=0, hi=9999):
        return [[rng.randint(lo, hi) for _ in range(i + 1)] for i in range(n)]

    case("n=1", [[5]])
    case("n=1 값 0", [[0]])
    case("n=2", [[1], [2, 3]])
    case("전부 0", [[0] * (i + 1) for i in range(10)])
    case("전부 9999", [[9999] * (i + 1) for i in range(10)])
    case("왼쪽 끝 경로", [[1 if j == 0 else 0 for j in range(i + 1)] for i in range(8)])
    case("오른쪽 끝 경로", [[1 if j == i else 0 for j in range(i + 1)] for i in range(8)])
    for i in range(6):
        case(f"작은 랜덤 {i+1}", rand(rng.randint(1, 15), 0, rng.choice([9, 9999])))
    case("n=30 랜덤", rand(30))
    case("최대 n=500 랜덤", rand(500))
    case("최대 n=500 전부 9999", [[9999] * (i + 1) for i in range(500)])
    case("최대 n=500 작은 값", rand(500, 0, 9))
    return cases
