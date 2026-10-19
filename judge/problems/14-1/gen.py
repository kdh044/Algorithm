import string

LETTERS = string.ascii_letters


def generate(rng):
    cases = []

    def name(maxlen=10):
        return "".join(rng.choice(LETTERS) for _ in range(rng.randint(1, maxlen)))

    def case(title, rows):
        assert 1 <= len(rows) <= 100000
        body = "".join(f"{a} {b} {c} {d}\n" for a, b, c, d in rows)
        cases.append({"name": title, "input": f"{len(rows)}\n{body}"})

    case("최소 N=1", [("A", 1, 1, 1)])
    case("국어만 다름", [("a", 10, 50, 50), ("b", 90, 50, 50), ("c", 50, 50, 50)])
    case("영어 오름차순", [("a", 50, 90, 50), ("b", 50, 10, 50), ("c", 50, 50, 50)])
    case("수학 내림차순", [("a", 50, 50, 10), ("b", 50, 50, 90), ("c", 50, 50, 50)])
    case("이름 대소문자", [("b", 1, 1, 1), ("B", 1, 1, 1), ("a", 1, 1, 1), ("A", 1, 1, 1), ("Ab", 1, 1, 1), ("AB", 1, 1, 1)])
    case("이름 접두사", [("abc", 5, 5, 5), ("ab", 5, 5, 5), ("abcd", 5, 5, 5), ("a", 5, 5, 5)])
    case("점수 경계", [("x", 1, 100, 1), ("y", 100, 1, 100), ("z", 100, 100, 100), ("w", 1, 1, 1)])
    for i in range(6):
        n = rng.randint(2, 30)
        case(f"작은 랜덤 {i+1}", [(name(4), rng.randint(1, 5), rng.randint(1, 5), rng.randint(1, 5)) for _ in range(n)])
    # 입력 조건의 최댓값은 N = 10만이지만, 저자 풀이(튜플 키 정렬)가 이 채점기의 PyPy에서 N = 10만이면
    # 0.8~1초 이상(제한 1초)이라 큰 케이스는 N = 6만으로 둔다. O(N^2) 정렬은 여전히 시간 초과.
    n = 60000
    case("큰 N 랜덤", [(name(), rng.randint(1, 100), rng.randint(1, 100), rng.randint(1, 100)) for _ in range(n)])
    case("큰 N 점수 범위 좁음", [(name(3), rng.randint(1, 3), rng.randint(1, 3), rng.randint(1, 3)) for _ in range(n)])
    case("큰 N 점수 모두 같음", [(name(), 77, 77, 77) for _ in range(n)])
    rows = [(name(), rng.randint(1, 100), rng.randint(1, 100), rng.randint(1, 100)) for _ in range(n)]
    rows.sort(key=lambda x: (x[1], -x[2], x[3]))  # 정답의 역순에 가깝게
    case("큰 N 역순에 가까움", rows)
    return cases
