MAXV = 1_000_000


def generate(rng):
    cases = []

    def case(name, arr):
        assert 1 <= len(arr) <= 1000 and all(1 <= x <= MAXV for x in arr)
        cases.append({"name": name, "input": f"{len(arr)}\n{' '.join(map(str, arr))}\n"})

    case("최소 N=1, 1원", [1])
    case("최소 N=1, 2원", [2])
    case("1원이 없음", [3, 5, 7])
    case("전부 1원", [1] * 10)
    case("최대 화폐 1개", [MAXV])
    case("2의 거듭제곱", [1 << i for i in range(20)])
    case("2의 거듭제곱 하나 빠짐", [1 << i for i in range(20) if i != 7])
    case("내림차순 입력", [10, 8, 4, 2, 1, 1])
    for i in range(6):
        n = rng.randint(2, 15)
        case(f"작은 랜덤 {i+1}", [rng.randint(1, 20) for _ in range(n)])
    n = 1000
    # 끝까지 다 만들 수 있는 경우(답 = 전체 합 + 1)
    arr = [1]
    s = 1
    while len(arr) < n:
        x = rng.randint(1, min(MAXV, s + 1))
        arr.append(x)
        s += x
    rng.shuffle(arr)
    case("최대 N 전부 연결", arr)
    case("최대 N 최대 화폐 + 1원", [1] + [MAXV] * (n - 1))
    case("최대 N 랜덤", [rng.randint(1, MAXV) for _ in range(n)])
    arr = [1] * 500 + [rng.randint(1, 1000) for _ in range(500)]
    rng.shuffle(arr)
    case("최대 N 작은 화폐", arr)
    case("최대 N 전부 최대", [MAXV] * n)
    return cases
