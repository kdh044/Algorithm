# 입력 조건의 최댓값: N = 100만, 높이 최대 10억. 순차 탐색(O(N * H))은 확실히 시간 초과.
BIG = 1000000
HMAX = 10 ** 9


def generate(rng):
    cases = []

    def case(name, arr, m):
        assert 1 <= m <= 2 * 10 ** 9 and sum(arr) >= m and all(0 <= x <= HMAX for x in arr)
        cases.append({"name": name, "input": f"{len(arr)} {m}\n{' '.join(map(str, arr))}\n"})

    case("최소 N=1, M=1", [1], 1)
    case("N=1, 높이 최대, M=1", [HMAX], 1)
    case("답이 0 (전부 가져가야 함)", [3, 5, 2, 7], 17)
    case("높이 0 섞임", [0, 0, 5, 0, 3], 4)
    case("전부 같은 높이", [10] * 8, 8)
    case("전부 같은 높이, 나누어떨어지지 않음", [10] * 8, 9)
    case("정렬된 높이", list(range(1, 21)), 50)
    case("역정렬 높이", list(range(20, 0, -1)), 37)
    for i in range(6):
        n = rng.randint(1, 30)
        arr = [rng.randint(0, 100) for _ in range(n)]
        if sum(arr) == 0:
            arr[0] = 1
        case(f"작은 랜덤 {i+1}", arr, rng.randint(1, sum(arr)))
    # 큰 케이스
    arr = [rng.randint(0, HMAX) for _ in range(BIG)]
    case("큰 N, 높이 최대 범위, M 작음", arr, rng.randint(1, 1000))
    arr = [rng.randint(0, HMAX) for _ in range(BIG)]
    case("큰 N, 높이 최대 범위, M 최대", arr, 2 * 10 ** 9)
    arr = [rng.randint(HMAX - 10 ** 6, HMAX) for _ in range(BIG)]
    case("큰 N, 높이가 10억 근처에 몰림", arr, rng.randint(10 ** 6, 2 * 10 ** 9))
    arr = [HMAX] * BIG
    case("큰 N, 전부 10억", arr, 1)
    arr = [rng.randint(0, 10 ** 6) for _ in range(1999)]
    case("N=1999, 답이 0", arr, sum(arr))
    arr = [rng.randint(0, 3000) for _ in range(BIG)]  # 합이 M 최대(20억) 이하가 되도록
    case("큰 N, 작은 높이, 답이 0 근처", arr, sum(arr) - rng.randint(0, BIG))
    return cases
