from itertools import combinations


def solve(g):
    n = len(g)
    sp = [(i, j) for i in range(n) for j in range(n) if g[i][j] == "X"]
    ts = [(i, j) for i in range(n) for j in range(n) if g[i][j] == "T"]
    for c in combinations(sp, 3):
        for i, j in c:
            g[i][j] = "O"
        seen = False
        for x, y in ts:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + dx, y + dy
                while 0 <= a < n and 0 <= b < n and g[a][b] not in "OT":
                    if g[a][b] == "S":
                        seen = True
                        break
                    a += dx; b += dy
                if seen:
                    break
            if seen:
                break
        for i, j in c:
            g[i][j] = "X"
        if not seen:
            return True
    return False


def generate(rng):
    cases = []
    want = {"YES": 0, "NO": 0}

    def case(name, rows):
        g = [r.split() for r in rows] if isinstance(rows[0], str) else rows
        n = len(g)
        assert 3 <= n <= 6 and sum(r.count("X") for r in g) >= 3
        cases.append({"name": name, "input": f"{n}\n" + "\n".join(" ".join(r) for r in g) + "\n"})
        return g

    def rand_grid(n, ts, ss):
        while True:
            g = [["X"] * n for _ in range(n)]
            pos = [(i, j) for i in range(n) for j in range(n)]
            rng.shuffle(pos)
            for i, j in pos[:ts]:
                g[i][j] = "T"
            for i, j in pos[ts:ts + ss]:
                g[i][j] = "S"
            if sum(r.count("X") for r in g) >= 3:
                return g

    case("빈칸 정확히 3개", ["T S S", "S X S", "X S X"])
    case("선생님과 학생이 붙어 있음", ["T S X", "X X X", "X X X"])
    case("학생이 숨어 있음", ["T X X", "X X X", "X X S"])
    case("한 줄에 막아야 할 곳이 많음", ["S X T X S", "X X X X X", "T X X X T", "X X X X X", "S X T X S"])
    case("최대 N 선생님 1명", ["T X X X X X", "X X X X X X", "X X X X X X", "X X X X X X", "X X X X X X", "X X X X X S"])
    case("최대 N 네 방향 감시", ["X X S X X X", "X X X X X X", "S X T X X S", "X X X X X X", "X X S X X X", "X X X X X X"])
    # YES/NO가 고루 나오도록 랜덤 생성
    for target, cnt in (("YES", 6), ("NO", 6)):
        made = 0
        while made < cnt:
            n = rng.randint(3, 6)
            g = rand_grid(n, rng.randint(1, max(1, n * n // 6)), rng.randint(1, max(1, n * n // 5)))
            ans = "YES" if solve([r[:] for r in g]) else "NO"
            if ans == target:
                made += 1
                case(f"랜덤 {target} {made}", g)
    # 최대 N, 빈칸이 많고 답이 NO (모든 조합을 다 확인해야 함)
    made = 0
    while made < 2:
        g = rand_grid(6, rng.randint(3, 5), rng.randint(2, 4))
        if not solve([r[:] for r in g]):
            made += 1
            case(f"최대 N 빈칸 많음 NO {made}", g)
    return cases
