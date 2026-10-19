from collections import deque


def reachable(board):
    n = len(board)
    W = n + 2
    b = [1] * (W * W)
    for i in range(n):
        for j in range(n):
            b[(i + 1) * W + j + 1] = board[i][j]
    goal = n * W + n
    seen = [[False] * (W * W), [False] * (W * W)]
    q = deque([(W + 1, 0)])
    seen[0][W + 1] = True
    while q:
        p, d = q.popleft()
        o = p + 1 if d == 0 else p + W
        if p == goal or o == goal:
            return True
        nxt = []
        for mv in (1, -1, W, -W):
            if b[p + mv] == 0 and b[o + mv] == 0:
                nxt.append((p + mv, d))
        if d == 0:
            if b[p - W] == 0 and b[p - W + 1] == 0:
                nxt += [(p - W, 1), (p - W + 1, 1)]
            if b[p + W] == 0 and b[p + W + 1] == 0:
                nxt += [(p, 1), (p + 1, 1)]
        else:
            if b[p - 1] == 0 and b[p + W - 1] == 0:
                nxt += [(p - 1, 0), (p + W - 1, 0)]
            if b[p + 1] == 0 and b[p + W + 1] == 0:
                nxt += [(p, 0), (p + W, 0)]
        for s, dd in nxt:
            if not seen[dd][s]:
                seen[dd][s] = True
                q.append((s, dd))
    return False


def generate(rng):
    cases = []

    def case(name, board):
        n = len(board)
        assert 5 <= n <= 100 and board[0][0] == 0 and board[0][1] == 0 and reachable(board)
        cases.append({"name": name, "args": [board]})

    def rand_board(n, p):
        while True:
            g = [[1 if rng.random() < p else 0 for _ in range(n)] for _ in range(n)]
            g[0][0] = g[0][1] = 0
            if reachable(g):
                return g

    def parse(rows):
        return [[int(c) for c in r] for r in rows]

    case("5x5 벽 없음", [[0] * 5 for _ in range(5)])
    case("세로로 세워야 통과", parse(["00000", "11001", "11101", "11100", "11100"]))
    case("폭 2 통로로 내려감", parse(["00000", "11100", "11100", "11100", "00000"]))
    case("회전 여러 번", parse(["00111", "00011", "10001", "11000", "11100"]))
    case("좁은 세로 통로로 도착", parse(["00011", "00000", "11100", "11100", "11110"]))
    for i in range(6):
        n = rng.randint(5, 12)
        case(f"작은 랜덤 {i+1}", rand_board(n, rng.choice([0.1, 0.2, 0.3])))
    for i in range(3):
        case(f"중간 랜덤 {i+1}", rand_board(rng.randint(30, 60), rng.choice([0.1, 0.2])))
    N = 100
    case("최대 N 벽 없음", [[0] * N for _ in range(N)])
    # 폭 2짜리 지그재그 통로 (경로 길이 최대화)
    g = [[0] * N for _ in range(N)]
    k = 0
    for r in range(2, N, 3):
        g[r] = [1] * N
        if k % 2 == 0:
            g[r][N - 2] = g[r][N - 1] = 0
        else:
            g[r][0] = g[r][1] = 0
        k += 1
    case("최대 N 지그재그 통로", g)
    # 세로 지그재그 (가로로는 못 지나가고 세로로 세워서 이동해야 하는 구간 포함)
    g = [[0] * N for _ in range(N)]
    for c in range(3, N - 1, 4):
        for r in range(N):
            g[r][c] = 1
        if (c // 4) % 2 == 0:
            g[N - 1][c] = g[N - 2][c] = 0
        else:
            g[0][c] = g[1][c] = 0
    case("최대 N 세로 칸막이", g)
    for i in range(3):
        case(f"최대 N 랜덤 {i+1}", rand_board(N, [0.05, 0.15, 0.25][i]))
    return cases
