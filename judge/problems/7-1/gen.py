LO, HI = 2, 1000000
# 입력 조건: N 최대 100만, 번호는 2 이상 100만 이하이고 부품 번호는 고유하므로 N은 실제로 최대 999,999.
BIG = HI - LO + 1  # 999,999 (가능한 모든 번호)


def generate(rng):
    cases = []

    def case(name, arr, qs):
        cases.append({"name": name, "input": f"{len(arr)}\n{' '.join(map(str, arr))}\n{len(qs)}\n{' '.join(map(str, qs))}\n"})

    case("최소 N=1 M=1 있음", [2], [2])
    case("최소 N=1 M=1 없음", [1000000], [2])
    case("경계값 번호", [2, 1000000], [1000000, 2, 3, 999999])
    case("전부 없음", [10, 20, 30], [11, 21, 31, 40])
    case("정렬된 부품", list(range(2, 52)), list(range(2, 60, 3)))
    case("역정렬 부품", list(range(51, 1, -1)), list(range(60, 1, -4)))
    for i in range(6):
        n = rng.randint(1, 30)
        arr = rng.sample(range(LO, 60), n)
        qs = rng.sample(range(LO, 60), rng.randint(1, 20))
        case(f"작은 랜덤 {i+1}", arr, qs)
    for i in range(2):
        n = rng.randint(1000, 5000)
        arr = rng.sample(range(LO, HI + 1), n)
        qs = rng.sample(arr, 300) + rng.sample(range(LO, HI + 1), 300)
        rng.shuffle(qs)
        case(f"중간 랜덤 {i+1}", arr, qs)
    # 큰 케이스 (N은 사실상 최대, M은 최대 10만)
    arr = list(range(LO, HI + 1))
    rng.shuffle(arr)
    case("최대 N(모든 번호), 질의 전부 yes", arr, [rng.randint(LO, HI) for _ in range(100000)])
    arr = rng.sample(range(LO, HI + 1), 900000)
    case("큰 N 랜덤, 질의 랜덤", arr, rng.sample(range(LO, HI + 1), 100000))
    arr = list(range(HI, LO - 1, -1))
    case("최대 N 역정렬", arr, [rng.randint(LO, HI) for _ in range(100000)])
    arr = rng.sample(range(LO, HI + 1), BIG - 100000)
    s = set(arr)
    absent = [v for v in range(LO, HI + 1) if v not in s]
    case("큰 N, 질의 전부 no", arr, rng.sample(absent, 100000))
    return cases
