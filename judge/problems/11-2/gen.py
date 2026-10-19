LIMIT = 2_000_000_000


def best(s):
    # 만들 수 있는 최댓값(입력 조건 '20억 이하' 확인용)
    r = int(s[0])
    for c in s[1:]:
        x = int(c)
        r = r + x if (x <= 1 or r <= 1) else r * x
    return r


def generate(rng):
    cases = []

    def case(name, s):
        assert 1 <= len(s) <= 20 and best(s) <= LIMIT, s
        cases.append({"name": name, "input": s + "\n"})

    def rand(length, digits):
        while True:
            s = "".join(rng.choice(digits) for _ in range(length))
            if best(s) <= LIMIT:
                return s

    case("한 자리 0", "0")
    case("한 자리 9", "9")
    case("한 자리 1", "1")
    case("전부 0", "0" * 20)
    case("전부 1", "1" * 20)
    case("1과 2", "12")
    case("2와 1", "21")
    case("1이 앞에", "1999")
    case("0이 중간", "9090909")
    case("2만 많이", "2" * 20)          # 2^20 = 1048576
    case("9 아홉 개", "9" * 9)           # 387420489
    case("1 뒤 9", "1" + "9" * 9)        # 2*9^9 = 774840978
    case("2 뒤 9", "2" + "9" * 9)        # 774840978
    case("20억 근접", "3" + "9" * 9)     # 1162261467
    for i in range(6):
        case(f"작은 랜덤 {i+1}", rand(rng.randint(2, 10), "0123456789"))
    for i in range(4):
        case(f"길이 20 랜덤 {i+1}", rand(20, "0011122"))
    case("길이 20 혼합", rand(20, "0123"))
    return cases
