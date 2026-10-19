def generate(rng):
    cases = []

    def case(name, arr):
        assert 1 <= len(arr) <= 500
        cases.append({"name": name, "input": f"{len(arr)}\n" + "".join(f"{x}\n" for x in arr)})

    case("N=1", [1])
    case("N=1 최댓값", [100000])
    case("전부 같은 값", [7] * 10)
    case("이미 내림차순", [9, 7, 5, 3, 1])
    case("오름차순", [1, 2, 3, 4, 5, 6])
    case("중복 섞임", [3, 1, 3, 2, 1, 3])
    for i in range(8):
        n = rng.randint(2, 30)
        case(f"작은 랜덤 {i+1}", [rng.randint(1, 100) for _ in range(n)])
    case("최대 N 랜덤", [rng.randint(1, 100000) for _ in range(500)])
    case("최대 N 오름차순", sorted(rng.randint(1, 100000) for _ in range(500)))
    case("최대 N 작은 값 중복", [rng.randint(1, 5) for _ in range(500)])
    case("최대 N 경계값", [rng.choice([1, 100000]) for _ in range(500)])
    return cases
