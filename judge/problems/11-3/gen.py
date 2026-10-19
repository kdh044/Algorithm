def generate(rng):
    cases = []

    def case(name, s):
        assert 1 <= len(s) < 1_000_000
        cases.append({"name": name, "input": s + "\n"})

    case("한 글자 0", "0")
    case("한 글자 1", "1")
    case("01", "01")
    case("10", "10")
    case("전부 같음", "1" * 50)
    case("양끝 1", "1000000001")
    case("010", "010")
    case("101", "101")
    case("교대 짝수", "01" * 10)
    case("교대 홀수", "10" * 10 + "1")
    for i in range(6):
        n = rng.randint(2, 40)
        case(f"작은 랜덤 {i+1}", "".join(rng.choice("01") for _ in range(n)))
    n = 999_999
    case("최대 교대", ("01" * (n // 2 + 1))[:n])
    case("최대 랜덤", "".join(rng.choice("01") for _ in range(n)))
    case("최대 전부 0", "0" * n)
    blocks = []
    total = 0
    while total < n:
        k = min(rng.randint(1, 3), n - total)
        blocks.append(("0" if len(blocks) % 2 == 0 else "1") * k)
        total += k
    case("최대 짧은 블록", "".join(blocks))
    return cases
