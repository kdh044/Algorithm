import heapq


def cost(arr):
    h = list(arr)
    heapq.heapify(h)
    r = 0
    while len(h) > 1:
        s = heapq.heappop(h) + heapq.heappop(h)
        r += s
        heapq.heappush(h, s)
    return r


def generate(rng):
    cases = []

    def case(name, arr):
        assert 1 <= len(arr) <= 100000 and all(1 <= x <= 1000 for x in arr)
        assert cost(arr) <= 2_100_000_000
        cases.append({"name": name, "input": f"{len(arr)}\n" + "".join(f"{x}\n" for x in arr)})

    case("최소 N=1", [50])
    case("N=2", [3, 7])
    case("전부 같음", [5] * 8)
    case("합친 묶음이 다시 최소", [1, 1, 1, 1, 100])
    case("내림차순", [40, 30, 20, 10])
    case("최대 크기", [1000, 1000, 1000])
    for i in range(6):
        n = rng.randint(2, 20)
        case(f"작은 랜덤 {i+1}", [rng.randint(1, 100) for _ in range(n)])
    n = 100000
    case("최대 N 랜덤", [rng.randint(1, 1000) for _ in range(n)])
    case("최대 N 전부 1", [1] * n)
    case("최대 N 오름차순", sorted(rng.randint(1, 1000) for _ in range(n)))
    case("최대 N 내림차순 큰 값", sorted((rng.randint(500, 1000) for _ in range(n)), reverse=True))
    return cases
