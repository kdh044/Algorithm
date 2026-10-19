import string


def generate(rng):
    cases = []
    used = set()

    def new_name(maxlen=10):
        while True:
            name = "".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, maxlen)))
            if name not in used:
                used.add(name)
                return name

    def case(name, students):
        # 성적이 같은 학생끼리는 이름 사전순으로 입력 순서를 맞춰,
        # 안정 정렬 / (성적, 이름) 정렬 모두 같은 답이 되게 한다.
        by = {}
        for nm, sc in students:
            by.setdefault(sc, []).append(nm)
        for sc in by:
            by[sc].sort()
        it = {sc: iter(v) for sc, v in by.items()}
        fixed = [(next(it[sc]), sc) for _, sc in students]
        assert 1 <= len(fixed) <= 100000
        assert all(1 <= len(nm) <= 100 and 1 <= sc <= 100 for nm, sc in fixed)
        cases.append({"name": name, "input": f"{len(fixed)}\n" + "".join(f"{nm} {sc}\n" for nm, sc in fixed)})
        used.clear()

    case("N=1", [(new_name(), 50)])
    case("두 명 같은 점수", [(new_name(), 70), (new_name(), 70)])
    case("이미 오름차순", [(new_name(), s) for s in [1, 20, 50, 100]])
    case("내림차순", [(new_name(), s) for s in [100, 90, 80, 10, 1]])
    case("이름 길이 100", [("a" * 100, 3), ("b" * 100, 1), ("c" * 99, 2)])
    case("전부 같은 점수", [(new_name(), 100) for _ in range(8)])
    for i in range(7):
        n = rng.randint(2, 30)
        case(f"작은 랜덤 {i+1}", [(new_name(), rng.randint(1, 100)) for _ in range(n)])
    N = 100000
    case("최대 N 랜덤", [(new_name(8), rng.randint(1, 100)) for _ in range(N)])
    case("최대 N 역순", [(new_name(8), 100 - i * 100 // N) for i in range(N)])
    case("최대 N 긴 이름", [(new_name(8) + "x" * 40, rng.randint(1, 100)) for _ in range(N)])
    return cases
