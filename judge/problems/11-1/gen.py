def generate(rng):
    cases = []
    def case(name, arr):
        cases.append({"name": name, "input": f"{len(arr)}\n{' '.join(map(str, arr))}\n"})
    case("최소 N=1", [1])
    case("그룹 불가", [2])
    case("전부 1", [1] * 10)
    case("전부 N", [7] * 7)
    for i in range(6):
        n = rng.randint(2, 30)
        case(f"작은 랜덤 {i+1}", [rng.randint(1, n) for _ in range(n)])
    n = 100000
    case("최대 N 랜덤", [rng.randint(1, n) for _ in range(n)])
    case("최대 N 작은 공포도", [rng.randint(1, 5) for _ in range(n)])
    case("최대 N 전부 1", [1] * n)
    case("최대 N 전부 N", [n] * n)
    return cases
