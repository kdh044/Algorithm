def generate(rng):
    cases = []

    def case(name, rows):
        n, m = len(rows), len(rows[0])
        assert 1 <= n <= 1000 and 1 <= m <= 1000
        cases.append({"name": name, "input": f"{n} {m}\n" + "".join(r + "\n" for r in rows)})

    def rand_rows(n, m, p):
        return ["".join('1' if rng.random() < p else '0' for _ in range(m)) for _ in range(n)]

    def snake(n, m):
        rows = []
        for i in range(n):
            if i % 2 == 0:
                rows.append('0' * m)
            else:
                gap = m - 1 if i % 4 == 1 else 0
                rows.append(''.join('0' if j == gap else '1' for j in range(m)))
        return rows

    case("1x1 구멍", ["0"])
    case("1x1 칸막이", ["1"])
    case("전부 칸막이", ["1" * 5] * 4)
    case("전부 구멍", ["0" * 6] * 3)
    case("한 줄", ["0101100010"])
    case("한 열", list("0010110"))
    case("체크 무늬 작게", ["01" * 3 if i % 2 == 0 else "10" * 3 for i in range(5)])
    case("뱀 모양 작게", snake(9, 7))
    for i in range(7):
        n, m = rng.randint(1, 15), rng.randint(1, 15)
        case(f"작은 랜덤 {i+1}", rand_rows(n, m, rng.choice([0.3, 0.5, 0.7])))
    N = M = 1000
    case("최대 전부 구멍", ["0" * M] * N)
    case("최대 랜덤", rand_rows(N, M, 0.45))
    case("최대 체크 무늬", ["01" * (M // 2) if i % 2 == 0 else "10" * (M // 2) for i in range(N)])
    case("최대 세로 줄무늬", ["01" * (M // 2)] * N)
    case("최대 뱀 모양", snake(N, M))
    return cases
