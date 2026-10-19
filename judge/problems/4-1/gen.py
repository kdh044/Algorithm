def generate(rng):
    cases = []

    def case(name, n, plan):
        assert 1 <= n <= 100 and 1 <= len(plan) <= 100
        cases.append({"name": name, "input": f"{n}\n{' '.join(plan)}\n"})

    case("N=1 모두 무시", 1, list("LRUDLRUD"))
    case("시작점에서 L, U 무시", 5, list("LLUU"))
    case("이동 1번", 3, ["D"])
    case("오른쪽 벽에 막힘", 4, ["R"] * 10)
    case("아래쪽 벽에 막힘 후 위로", 4, ["D"] * 10 + ["U"])
    case("한 바퀴", 3, list("RRDDLLUU"))
    case("오른쪽 아래 구석", 100, ["R"] * 50 + ["D"] * 50)
    for i in range(8):
        n = rng.randint(1, 10)
        case(f"작은 랜덤 {i+1}", n, [rng.choice("LRUD") for _ in range(rng.randint(1, 30))])
    for i, n in enumerate([2, 7, 100]):
        case(f"최대 이동 랜덤 {i+1}", n, [rng.choice("LRUD") for _ in range(100)])
    case("최대 이동 RD 위주", 100, [rng.choice("RRRDDDLU") for _ in range(100)])
    return cases
