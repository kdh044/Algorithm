def generate(rng):
    cases = []

    def case(name, p):
        assert len(p) % 2 == 0 and 2 <= len(p) <= 1000 and p.count("(") == p.count(")")
        cases.append({"name": name, "args": [p]})

    def rand_balanced(n):
        s = ["("] * (n // 2) + [")"] * (n // 2)
        rng.shuffle(s)
        return "".join(s)

    def rand_proper(n):
        out, open_, left = [], 0, n // 2
        while len(out) < n:
            if left and (open_ == 0 or rng.random() < 0.5):
                out.append("("); open_ += 1; left -= 1
            else:
                out.append(")"); open_ -= 1
        return "".join(out)

    case("최소 올바름", "()")
    case("최소 뒤집힘", ")(")
    case("짧은 예", "))((")
    case("짧은 예 2", ")()(")
    case("짧은 예 3", "())(()")
    for i in range(6):
        case(f"작은 랜덤 {i+1}", rand_balanced(rng.randrange(2, 21, 2)))
    for i in range(3):
        case(f"중간 랜덤 {i+1}", rand_balanced(rng.randrange(50, 201, 2)))
    case("최대 길이 이미 올바름", rand_proper(1000))
    case("최대 길이 깊은 중첩", "(" * 500 + ")" * 500)
    case("최대 길이 전부 뒤집힘", ")" * 500 + "(" * 500)
    case("최대 길이 )( 반복", ")(" * 500)
    case("최대 길이 () 반복", "()" * 500)
    for i in range(3):
        case(f"최대 길이 랜덤 {i+1}", rand_balanced(1000))
    return cases
