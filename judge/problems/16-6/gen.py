LOWER = "abcdefghijklmnopqrstuvwxyz"
LETTERS = LOWER + LOWER.upper()


def generate(rng):
    cases = []

    def case(name, a, b):
        cases.append({"name": name, "input": f"{a}\n{b}\n"})

    def rs(n, alpha):
        return "".join(rng.choice(alpha) for _ in range(n))

    case("길이 1 같음", "a", "a")
    case("길이 1 다름", "a", "b")
    case("대소문자 구분", "abc", "ABC")
    case("완전히 다른 문자", "aaaa", "bbbbbbb")
    case("삽입만", "ace", "abcde")
    case("삭제만", "abcde", "ace")
    case("같은 문자열", "kitten", "kitten")
    case("kitten/sitting", "kitten", "sitting")
    for i in range(6):
        case(f"작은 랜덤 {i+1}", rs(rng.randint(1, 8), "ab"), rs(rng.randint(1, 8), "abc"))
    case("중간 랜덤", rs(300, LETTERS), rs(250, LETTERS))
    case("최대 5000x5000 (ab)", rs(5000, "ab"), rs(5000, "ab"))
    case("최대 5000x5000 (알파벳)", rs(5000, LETTERS), rs(5000, LETTERS))
    a = rs(5000, "abc")
    case("길이 5000 x 800", a, rs(800, "abc"))
    case("길이 5000 x 1", a, "a")
    s = rs(5000, "ab")
    t = list(s)
    for _ in range(100):
        t[rng.randrange(len(t))] = rng.choice("ab")
    case("최대 5000x5000 거의 같은 문자열", s, "".join(t))
    return cases
