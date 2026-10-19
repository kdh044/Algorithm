def generate(rng):
    cases = []

    def case(name, arr):
        cases.append({"name": name, "input": f"{len(arr)}\n{' '.join(map(str, arr))}\n"})

    case("N=1", [5])
    case("N=2 내림차순", [2, 1])
    case("N=2 같음", [3, 3])
    case("이미 내림차순", list(range(10, 0, -1)))
    case("오름차순", list(range(1, 11)))
    case("전부 같음", [7] * 10)
    case("최댓값 전투력", [10**7, 1, 10**7, 1])
    for i in range(6):
        n = rng.randint(1, 14)
        case(f"작은 랜덤 {i+1}", [rng.randint(1, rng.choice([5, 100])) for _ in range(n)])
    n = 2000
    case("최대 N 랜덤", [rng.randint(1, 10**7) for _ in range(n)])
    case("최대 N 중복 많음", [rng.randint(1, 50) for _ in range(n)])
    case("최대 N 내림차순", list(range(10**7, 10**7 - n, -1)))
    case("최대 N 오름차순", list(range(1, n + 1)))
    arr = list(range(n, 0, -1))
    for _ in range(100):
        i, j = rng.randrange(n), rng.randrange(n)
        arr[i], arr[j] = arr[j], arr[i]
    case("최대 N 거의 내림차순", arr)
    return cases
