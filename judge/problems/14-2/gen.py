MAXV = 100000


def generate(rng):
    cases = []

    def case(name, arr):
        assert 1 <= len(arr) <= 200000 and all(1 <= x <= MAXV for x in arr)
        cases.append({"name": name, "input": f"{len(arr)}\n{' '.join(map(str, arr))}\n"})

    case("최소 N=1", [7])
    case("N=2 (작은 값)", [10, 3])
    case("N=2 같은 위치", [4, 4])
    case("전부 같은 위치", [5] * 6)
    case("짝수 개 중간 두 값", [1, 2, 3, 4, 5, 6])
    case("홀수 개", [9, 1, 5])
    case("한쪽에 몰림", [1, 1, 1, 100000, 100000])
    for i in range(6):
        n = rng.randint(2, 20)
        case(f"작은 랜덤 {i+1}", [rng.randint(1, 30) for _ in range(n)])
    n = 200000
    case("최대 N 랜덤", [rng.randint(1, MAXV) for _ in range(n)])
    arr = list(range(1, MAXV + 1)) * 2
    rng.shuffle(arr)
    case("최대 N 모든 위치 2채씩", arr)
    case("최대 N 역정렬", sorted([rng.randint(1, MAXV) for _ in range(n)], reverse=True))
    case("최대 N 두 위치", [1] * (n // 2) + [MAXV] * (n // 2))
    return cases
