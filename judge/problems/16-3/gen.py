def generate(rng):
    cases = []

    def case(name, tp):
        cases.append({"name": name, "input": f"{len(tp)}\n" + "\n".join(f"{t} {p}" for t, p in tp) + "\n"})

    case("N=1 가능", [(1, 7)])
    case("N=1 불가능", [(2, 7)])
    case("전부 기간 초과", [(5, 1000)] * 4)
    case("마지막 날 1일 상담", [(5, 1), (5, 1), (5, 1), (5, 1), (1, 1000)])
    case("전부 1일", [(1, 1000)] * 15)
    case("전부 5일", [(5, 1000)] * 15)
    case("탐욕 반례", [(2, 10), (1, 6), (1, 6)])
    for i in range(8):
        n = rng.randint(1, 15)
        case(f"랜덤 {i+1}", [(rng.randint(1, 5), rng.randint(1, 1000)) for _ in range(n)])
    for i in range(3):
        case(f"최대 N=15 랜덤 {i+1}", [(rng.randint(1, 5), rng.randint(1, 1000)) for _ in range(15)])
    return cases
