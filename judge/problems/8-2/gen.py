def generate(rng):
    cases = []

    def case(name, arr):
        cases.append({"name": name, "input": f"{len(arr)}\n{' '.join(map(str, arr))}\n"})

    case("최소 N=3", [1, 2, 3])
    case("N=3 가운데가 큼", [1, 5, 1])
    case("전부 0", [0] * 10)
    case("전부 같은 값", [7] * 9)
    case("전부 1000 (N=100)", [1000] * 100)
    case("정렬", list(range(0, 20)))
    case("역정렬", list(range(19, -1, -1)))
    case("두 칸 건너뛰는 게 이득", [5, 1, 1, 5])
    case("홀짝 교대가 아닌 최적", [10, 1, 1, 10, 1, 1, 10])
    for i in range(6):
        n = rng.randint(3, 15)
        case(f"작은 랜덤 {i+1}", [rng.randint(0, 20) for _ in range(n)])
    for i in range(3):
        case(f"최대 N=100 랜덤 {i+1}", [rng.randint(0, 1000) for _ in range(100)])
    case("최대 N=100, 0과 1000 섞임", [rng.choice([0, 1000]) for _ in range(100)])
    return cases
