def generate(rng):
    cases = []

    def case(name, pts):
        lines = [str(len(pts))] + [f"{x} {y} {z}" for x, y, z in pts]
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    def distinct(n, lo, hi):
        s = set()
        while len(s) < n:
            s.add((rng.randint(lo, hi), rng.randint(lo, hi), rng.randint(lo, hi)))
        s = list(s)
        rng.shuffle(s)
        return s

    L = 10 ** 9
    case("N=1 (비용 0)", [(5, -3, 7)])
    case("N=2", [(0, 0, 0), (10, 20, 30)])
    case("N=2 최대 좌표 차이", [(-L, -L, -L), (L, L, L)])
    case("한 좌표가 같은 행성들 (비용 0)", [(1, 2, 3), (1, 5, 9), (1, -4, 0), (1, 100, -100)])
    case("x축 위의 점들", [(x, 0, 0) for x in (5, -2, 9, 0, 3)])
    for i in range(7):
        n = rng.randint(2, 30)
        case(f"작은 랜덤 {i+1}", distinct(n, -rng.choice([5, 100, L]), rng.choice([5, 100, L])))
    # 입력 조건의 최댓값은 N = 10만이지만, 저자 풀이(튜플 정렬 4번)가 이 채점기의 PyPy에서 N = 10만이면
    # 1.2~1.8초(제한 1초)라 큰 케이스는 N = 3만으로 둔다. O(N^2) 프림은 N = 3만에서도 20초 이상 걸려 시간 초과.
    N = 30000
    case("큰 N 넓은 좌표", distinct(N, -L, L))
    case("큰 N 좁은 좌표 (동률 다수)", distinct(N, -30, 30))
    xs = rng.sample(range(-L, L + 1), N)
    case("큰 N 한 직선 위 (y, z 동일)", [(x, 7, -7) for x in xs])
    pts = [(i * 20000 - L, -i * 20000 + L, (i * 7919) % 200001 * 10000 - L) for i in range(N)]
    rng.shuffle(pts)
    case("큰 N 대각선 배치 큰 비용", pts)
    return cases
