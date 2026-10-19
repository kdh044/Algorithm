def generate(rng):
    cases = []
    def case(name, xs, c):
        xs = list(xs)
        rng.shuffle(xs)
        cases.append({"name": name, "input": f"{len(xs)} {c}\n" + "\n".join(map(str, xs)) + "\n"})
    case("N=2 C=2 인접", [1, 2], 2)
    case("N=2 C=2", [3, 50], 2)
    case("연속 좌표 C=N", range(1, 11), 10)
    case("연속 좌표 C=2", range(1, 11), 2)
    case("C=N 불균등", [1, 2, 10, 30, 31, 100], 6)
    case("정렬 안 된 입력", [9, 1, 8, 4, 2], 3)
    for i in range(7):
        n = rng.randint(2, 15)
        xs = rng.sample(range(1, 60), n)
        case(f"작은 랜덤 {i+1}", xs, rng.randint(2, n))
    n = 200000
    xs = rng.sample(range(1, 10**9 + 1), n)
    case("최대 N C=1000", xs, 1000)
    case("최대 N C=3", xs, 3)
    case("최대 N C=24000", xs, 24000)
    case("최대 N C=30000", xs, 30000)
    case("최대 N C=N", rng.sample(range(1, 4 * n), n), n)
    xs = [1, 10**9] + rng.sample(range(2, 10**9), n - 2)
    case("최대 N 양 끝 포함 C=2", xs, 2)
    case("최대 N 등간격 C=N", range(1, 10**9, 5000), n)
    return cases
