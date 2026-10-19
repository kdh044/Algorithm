import string

L = string.ascii_lowercase


def generate(rng):
    cases = []
    def case(name, s):
        assert 1 <= len(s) <= 1000 and s.isalpha() and s.islower()
        cases.append({"name": name, "args": [s]})

    def rnd(n, alpha):
        return "".join(rng.choice(alpha) for _ in range(n))

    def periodic(n, period, alpha):
        unit = rnd(period, alpha)
        return (unit * (n // period + 1))[:n]

    case("길이 1", "a")
    case("길이 2 같은 문자", "zz")
    case("길이 2 다른 문자", "ab")
    case("길이 3", "aab")
    case("10번 반복(두 자리 수)", "a" * 10)
    case("100번 반복(세 자리 수)", "ab" * 100)
    for i in range(6):
        n = rng.randint(4, 40)
        case(f"작은 랜덤 {i+1}", rnd(n, rng.choice(["ab", "abc", L])))
    for i in range(3):
        n = rng.randint(20, 60)
        case(f"작은 주기 문자열 {i+1}", periodic(n, rng.randint(2, 6), "ab"))
    n = 1000
    case("최대 길이 같은 문자", "a" * n)
    case("최대 길이 랜덤(ab)", rnd(n, "ab"))
    case("최대 길이 랜덤(26자)", rnd(n, L))
    case("최대 길이 주기 7", periodic(n, 7, L))
    case("최대 길이 주기 500", periodic(n, 500, L))
    case("최대 길이 블록 반복", "".join(c * rng.randint(1, 30) for c in rnd(200, "abc"))[:n].ljust(n, "a"))
    return cases
