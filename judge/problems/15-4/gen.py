def generate(rng):
    cases = []

    def rword(length, alpha):
        return "".join(rng.choice(alpha) for _ in range(length))

    def words_of(lengths, alpha):
        seen = set()
        out = []
        for L in lengths:
            for _ in range(50):
                w = rword(L, alpha)
                if w not in seen:
                    break
            else:
                continue
            seen.add(w)
            out.append(w)
        return out

    def query_from(w, alpha):
        L = len(w)
        k = rng.randint(1, L)  # '?' 개수
        if rng.random() < 0.7:
            base = w
        else:
            base = rword(L, alpha)
        if rng.random() < 0.5:
            return base[:L - k] + "?" * k
        return "?" * k + base[k:]

    def case(name, words, queries):
        cases.append({"name": name, "args": [words, queries]})

    case("최소", ["a", "b"], ["?", "??"])
    case("전부 ?", ["abc", "abd", "xy", "z"], ["???", "??", "?", "????"])
    case("접두사 ?", ["abc", "bbc", "cbc", "abd"], ["?bc", "??c", "??d", "?bd"])
    case("접미사 ?", ["abc", "abd", "acd", "bcd"], ["ab?", "a??", "b??", "c??"])
    case("길이 불일치", ["aaaa", "aaaaa"], ["aaa?", "aaaa?", "aaaaa?", "?aaaaaa"])
    case("중복 키워드", ["hello", "hella", "world"], ["hell?", "hell?", "?????", "?????"])
    for i in range(6):
        alpha = "ab" if i % 2 == 0 else "abc"
        words = words_of([rng.randint(1, 6) for _ in range(rng.randint(2, 30))], alpha)
        if len(words) < 2:
            words = ["a", "b"]
        queries = [query_from(rng.choice(words), alpha) for _ in range(rng.randint(2, 30))]
        case(f"작은 랜덤 {i+1}", words, queries)

    alpha = "abcd"
    words = words_of([10] * 100000, alpha)
    queries = [query_from(rng.choice(words), alpha) for _ in range(100000)]
    case("최대: 길이 10 단어/키워드 10만 개", words, queries)

    queries = ["?" * rng.randint(1, 9) + w[-1] if rng.random() < 0.5 else w[0] + "?" * 9 for w in (rng.choice(words) for _ in range(100000))]
    queries = [q if len(q) == 10 else q.rjust(10, "?") for q in queries]
    case("최대: 매치 많은 키워드", words, queries)

    alpha = "ab"
    words = words_of([10000] * 100, alpha)
    queries = [query_from(rng.choice(words), alpha) for _ in range(100)]
    case("최대: 길이 10000 단어 100개", words, queries)

    lengths = []
    total = 0
    while len(lengths) < 100000:
        L = rng.choice([rng.randint(1, 20), rng.randint(5, 12)])
        if total + L > 1000000:
            break
        lengths.append(L)
        total += L
    alpha = "abcdefghijklmnopqrstuvwxyz"
    words = words_of(lengths, alpha)
    queries = []
    total = 0
    while len(queries) < 100000:
        q = query_from(rng.choice(words), alpha)
        if total + len(q) > 1000000:
            break
        queries.append(q)
        total += len(q)
    case("최대: 길이 혼합", words, queries)
    return cases
