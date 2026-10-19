def generate(rng):
    cases = []

    def case(name, m, coins):
        assert 1 <= len(coins) <= 100 and 1 <= m <= 10000 and all(1 <= c <= 10000 for c in coins)
        cases.append({"name": name, "input": f"{len(coins)} {m}\n" + "".join(f"{c}\n" for c in coins)})

    case("최소 N=1 M=1", 1, [1])
    case("N=1 불가능", 1, [2])
    case("화폐가 M보다 큼", 5, [6, 10000])
    case("M과 같은 화폐", 10000, [10000])
    case("그리디 반례", 6, [1, 3, 4])
    case("그리디 반례 2", 30, [1, 15, 25])
    case("짝수 화폐로 홀수 불가", 9999, [2, 4, 6, 8])
    case("1원 화폐만, M 최대", 10000, [1])
    for i in range(6):
        n = rng.randint(1, 5)
        case(f"작은 랜덤 {i+1}", rng.randint(1, 60), rng.sample(range(1, 30), n))
    # 최대 크기: N=100, M=10000, 화폐 단위가 작아 모든 금액을 확인해야 함
    case("최대 N, M, 작은 화폐", 10000, rng.sample(range(1, 201), 100))
    case("최대 N, M, 1~100", 10000, list(range(1, 101)))
    case("최대 N, M, 큰 화폐 위주", 10000, rng.sample(range(97, 10001), 100))
    case("최대 N, M, 불가능 (모두 짝수)", 9999, rng.sample(range(2, 1001, 2), 100))
    case("최대 N, M, 서로소 큰 값 두 개 + 큰 값들", 9973, [97, 89] + rng.sample(range(5000, 10001), 98))
    return cases
