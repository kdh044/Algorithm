def generate(rng):
    cases = []
    def case(name, n):
        s = str(n)
        assert 10 <= n <= 99999999 and len(s) % 2 == 0
        cases.append({"name": name, "input": s + "\n"})

    def lucky(digits):
        # 왼쪽 합 == 오른쪽 합이 되도록 생성
        h = digits // 2
        while True:
            left = [rng.randint(1, 9)] + [rng.randint(0, 9) for _ in range(h - 1)]
            target = sum(left)
            if target > 9 * h:
                continue
            right = [0] * h
            rem = target
            idx = list(range(h))
            rng.shuffle(idx)
            for i in idx:
                v = min(9, rem)
                v = rng.randint(max(0, rem - 9 * (h - 1 - idx.index(i))), v) if rem else 0
                right[i] = v
                rem -= v
            if rem == 0:
                return int("".join(map(str, left + right)))

    case("최솟값 10", 10)
    case("11 LUCKY", 11)
    case("99 LUCKY", 99)
    case("최댓값 99999999", 99999999)
    case("10000000", 10000000)
    case("10000001 LUCKY", 10000001)
    case("1001 LUCKY", 1001)
    case("100000", 100000)
    for d in (2, 4, 6, 8):
        for i in range(2):
            case(f"{d}자리 LUCKY {i+1}", lucky(d))
        for i in range(2):
            case(f"{d}자리 랜덤 {i+1}", rng.randint(10 ** (d - 1), 10 ** d - 1))
    return cases
