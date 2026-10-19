def generate(rng):
    cases = []
    def case(name, key, lock):
        m, n = len(key), len(lock)
        assert 3 <= m <= n <= 20
        assert all(len(r) == m for r in key) and all(len(r) == n for r in lock)
        cases.append({"name": name, "args": [key, lock]})

    def rand_grid(s, p):
        return [[1 if rng.random() < p else 0 for _ in range(s)] for _ in range(s)]

    def rot(a):
        s = len(a)
        return [[a[s - 1 - j][i] for j in range(s)] for i in range(s)]

    def make_true(n, m, p, rotate=True):
        # 열쇠를 회전/이동한 모양에 맞춰 자물쇠를 만든다(정답 true)
        key = rand_grid(m, p)
        k = key
        if rotate:
            for _ in range(rng.randint(0, 3)):
                k = rot(k)
        lock = [[1] * n for _ in range(n)]
        dx = rng.randint(-(m - 1), n - 1)
        dy = rng.randint(-(m - 1), n - 1)
        for i in range(m):
            for j in range(m):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n:
                    lock[x][y] = 1 - k[i][j]
        return key, lock

    def near_true(n, m, p):
        # 정답 모양에서 자물쇠 한 칸을 뒤집어 대부분 false가 되게
        key, lock = make_true(n, m, p)
        x, y = rng.randrange(n), rng.randrange(n)
        lock[x][y] ^= 1
        return key, lock

    # 경계
    case("최소 크기, 홈 없음", [[0] * 3 for _ in range(3)], [[1] * 3 for _ in range(3)])
    case("최소 크기, 열쇠 돌기 없음", [[0] * 3 for _ in range(3)], [[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    case("최소 크기, 자물쇠 전부 홈 + 열쇠 전부 돌기", [[1] * 3 for _ in range(3)], [[0] * 3 for _ in range(3)])
    case("자물쇠 전부 홈 + 열쇠가 더 작음", [[1] * 3 for _ in range(3)], [[0] * 4 for _ in range(4)])
    case("열쇠 일부만 걸침(모서리)", [[0, 0, 0], [0, 0, 0], [0, 0, 1]], [[0, 1, 1], [1, 1, 1], [1, 1, 1]])
    case("돌기끼리 충돌", [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    # 작은 랜덤
    for i in range(4):
        n = rng.randint(3, 8); m = rng.randint(3, n)
        key, lock = make_true(n, m, rng.choice([0.3, 0.5, 0.7]))
        case(f"작은 true {i+1}", key, lock)
    for i in range(4):
        n = rng.randint(3, 8); m = rng.randint(3, n)
        key, lock = near_true(n, m, rng.choice([0.3, 0.5, 0.7]))
        case(f"작은 거의 true {i+1}", key, lock)
    for i in range(2):
        n = rng.randint(3, 8); m = rng.randint(3, n)
        case(f"작은 랜덤 {i+1}", rand_grid(m, 0.5), rand_grid(n, 0.8))
    # 최대 크기
    key, lock = make_true(20, 20, 0.5)
    case("최대 N=M=20 true", key, lock)
    key, lock = make_true(20, 7, 0.6)
    case("최대 N=20, M=7 true", key, lock)
    key, lock = near_true(20, 20, 0.5)
    case("최대 N=M=20 한 칸 어긋남", key, lock)
    key = [[0] * 20 for _ in range(20)]; key[0][0] = 1
    lock = [[1] * 20 for _ in range(20)]; lock[0][0] = 0; lock[19][19] = 0
    case("최대, 멀리 떨어진 두 홈(false, 전체 탐색)", key, lock)
    key = [[1] * 20 for _ in range(20)]
    lock = [[0] * 20 for _ in range(20)]; lock[19][19] = 1
    case("최대, 열쇠 전부 돌기 + 자물쇠 한 칸만 돌기(false)", key, lock)
    key = [[1] * 20 for _ in range(20)]; key[19][19] = 0
    lock = [[0] * 20 for _ in range(20)]; lock[0][0] = 1
    case("최대, 회전해야 맞음(true)", key, lock)
    return cases
