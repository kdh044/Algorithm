import string

U = string.ascii_uppercase
D = string.digits


def generate(rng):
    cases = []
    def case(name, s):
        assert 1 <= len(s) <= 10000
        # 숫자가 있으면 합이 0이 되지 않도록(출력 형식이 모호해지는 경우 배제)
        if any(c.isdigit() for c in s):
            assert any(c in "123456789" for c in s)
        cases.append({"name": name, "input": s + "\n"})

    def rand(n, p_digit):
        s = [rng.choice(D) if rng.random() < p_digit else rng.choice(U) for _ in range(n)]
        if any(c.isdigit() for c in s) and not any(c in "123456789" for c in s):
            s[rng.randrange(n)] = rng.choice("123456789")
        return "".join(s)

    case("길이 1 알파벳", "Q")
    case("길이 1 숫자", "7")
    case("알파벳만", "ZYXWVUTSRQPONMLKJIHGFEDCBA")
    case("숫자만", "9081726354")
    case("숫자 하나 + 0들", "A0B0C1")
    case("이미 정렬됨", "AABBCC123")
    for i in range(6):
        case(f"작은 랜덤 {i+1}", rand(rng.randint(2, 30), rng.choice([0.2, 0.5, 0.8])))
    n = 10000
    case("최대 길이 랜덤", rand(n, 0.5))
    case("최대 길이 알파벳만", rand(n, 0))
    case("최대 길이 숫자만(전부 9)", "9" * n)
    case("최대 길이 역정렬 알파벳", "".join(sorted(rand(n, 0), reverse=True)))
    case("최대 길이 같은 문자 + 숫자 1", "A" * (n - 1) + "1")
    return cases
