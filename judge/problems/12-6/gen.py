def ok_item(S, x, y, a):
    if a == 0:
        return y == 0 or (x - 1, y, 1) in S or (x, y, 1) in S or (x, y - 1, 0) in S
    return (x, y - 1, 0) in S or (x + 1, y - 1, 0) in S or ((x - 1, y, 1) in S and (x + 1, y, 1) in S)


def affected(x, y, a):
    if a == 0:
        return [(x, y + 1, 0), (x - 1, y + 1, 1), (x, y + 1, 1)]
    return [(x, y, 0), (x + 1, y, 0), (x - 1, y, 1), (x + 1, y, 1)]


class Sim:
    def __init__(self, n):
        self.n = n
        self.S = set()
        self.ops = []

    def rand_item(self, rng):
        n = self.n
        if rng.random() < 0.5:
            return (rng.randint(0, n), rng.randint(0, n - 1), 0)
        return (rng.randint(0, n - 1), rng.randint(1, n), 1)

    def install(self, it):
        assert it not in self.S
        x, y, a = it
        n = self.n
        assert (a == 0 and 0 <= x <= n and 0 <= y <= n - 1) or (a == 1 and 0 <= x <= n - 1 and 1 <= y <= n)
        self.ops.append([x, y, a, 1])
        if ok_item(self.S, *it):
            self.S.add(it)
            return True
        return False

    def delete(self, it):
        assert it in self.S
        self.ops.append([it[0], it[1], it[2], 0])
        self.S.remove(it)
        if all(ok_item(self.S, *b) for b in affected(*it) if b in self.S):
            return True
        self.S.add(it)
        return False

    def random_install(self, rng):
        for _ in range(2000):
            it = self.rand_item(rng)
            if it not in self.S:
                return self.install(it)
        return self.delete(rng.choice(sorted(self.S)))  # 빈 자리가 없으면 삭제

    def good_install(self, rng, tries=300):
        for _ in range(tries):
            it = self.rand_item(rng)
            if it not in self.S and ok_item(self.S, *it):
                return self.install(it)
        return self.random_install(rng)

    def random_delete(self, rng):
        if not self.S:
            return self.random_install(rng)
        return self.delete(rng.choice(sorted(self.S)))


def mixed(rng, n, m, p_good, p_del):
    sim = Sim(n)
    while len(sim.ops) < m:
        r = rng.random()
        if r < p_del:
            sim.random_delete(rng)
        elif r < p_del + p_good:
            sim.good_install(rng)
        else:
            sim.random_install(rng)
    return sim.ops


def generate(rng):
    cases = []
    def case(name, n, ops):
        assert 5 <= n <= 100 and 1 <= len(ops) <= 1000
        cases.append({"name": name, "args": [n, ops]})

    case("작업 1개: 바닥 기둥", 5, [[0, 0, 0, 1]])
    case("작업 1개: 공중 보(무시됨)", 5, [[2, 3, 1, 1]])
    case("설치 후 삭제", 5, [[0, 0, 0, 1], [0, 0, 0, 0]])
    case("보 위 기둥이 있어 삭제 불가", 5, [[0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 0, 0]])
    case("양쪽 보로 지탱되는 보", 5, [[0, 0, 0, 1], [3, 0, 0, 1], [0, 1, 1, 1], [2, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [3, 0, 0, 0]])
    case("벽 끝 좌표(x=n 기둥, y=n 보)", 5, [[5, 0, 0, 1], [5, 1, 0, 1], [5, 2, 0, 1], [5, 3, 0, 1], [5, 4, 0, 1], [4, 5, 1, 1], [3, 5, 1, 1], [5, 4, 0, 0]])
    for i in range(4):
        n = rng.randint(5, 8)
        case(f"작은 랜덤 {i+1}", n, mixed(rng, n, rng.randint(10, 40), 0.5, 0.25))
    for i in range(2):
        n = rng.randint(5, 20)
        case(f"중간 랜덤 {i+1}", n, mixed(rng, n, rng.randint(100, 300), 0.5, 0.3))
    # 최대 크기
    n = 100
    # 격자형 구조물(기둥 101개 + 보 100개를 한 층씩)
    ops = []
    for y in range(0, 5):
        for x in range(0, 101):
            ops.append([x, y, 0, 1])
        for x in range(0, 100):
            ops.append([x, y + 1, 1, 1])
    # 격자 750개 설치 + 지지대 없는 공중 보 설치 시도 250개(무시됨)
    air = [[x, 50, 1, 1] for x in range(0, 100, 2)] * 5
    case("최대: 격자 750개 설치 + 공중 보 시도 250개", n, ops[:750] + air)
    case("최대: 설치 위주 랜덤(구조물 많음)", n, mixed(rng, n, 1000, 0.75, 0.2))
    case("최대: 설치/삭제 혼합", n, mixed(rng, n, 1000, 0.6, 0.3))
    ops = ops[:700]
    order = [list(o) for o in ops]
    rng.shuffle(order)
    for o in order[:300]:
        ops.append([o[0], o[1], o[2], 0])
    case("최대: 격자 700개 설치 후 300개 삭제 시도", n, ops)
    # 기둥 탑 10개 x 높이 30 설치 후 삭제 시도(위에서부터가 아닌 삭제는 무시됨)
    ops = [[x, y, 0, 1] for x in range(0, 100, 10) for y in range(30)]
    dels = [[x, y, 0, 0] for y in range(29, -1, -1) for x in range(0, 100, 10)]
    tail = dels[100:300]
    rng.shuffle(tail)
    ops += dels[:100] + tail
    case("최대: 기둥 탑 300개 설치 후 삭제 시도", n, ops)
    case("최대 작업, 작은 벽면 n=5", 5, mixed(rng, 5, 1000, 0.4, 0.4))
    return cases
