def generate(rng):
    cases = []
    def case(name, arr, x):
        cases.append({"name": name, "input": f"{len(arr)} {x}\n{' '.join(map(str, arr))}\n"})
    case("N=1 있음", [5], 5)
    case("N=1 없음", [5], 4)
    case("전부 x", [7] * 10, 7)
    case("x가 맨 앞", [-3, -3, 0, 1, 2], -3)
    case("x가 맨 뒤", [-3, 0, 1, 2, 2], 2)
    case("x가 최솟값보다 작음", [1, 2, 3], -10**9)
    case("x가 최댓값보다 큼", [1, 2, 3], 10**9)
    case("극값 원소", [-10**9, -10**9, 0, 10**9], 10**9)
    case("사이 값 없음", [1, 1, 3, 3], 2)
    for i in range(6):
        n = rng.randint(1, 30)
        arr = sorted(rng.randint(-5, 5) for _ in range(n))
        case(f"작은 랜덤 {i+1}", arr, rng.randint(-6, 6))
    n = 10**6
    arr = sorted(rng.randint(-10**6, 10**6) for _ in range(n))
    case("최대 N 랜덤(있음)", arr, arr[n // 2])
    case("최대 N 랜덤(없음)", arr, 10**6 + 1)
    arr = sorted(rng.randint(-50, 50) for _ in range(n))
    case("최대 N 중복 많음", arr, 0)
    case("최대 N 전부 x", [-10**9] * n, -10**9)
    return cases
