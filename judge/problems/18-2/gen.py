def generate(rng):
    cases = []

    def case(name, g, planes):
        cases.append({"name": name, "input": f"{g}\n{len(planes)}\n" + "\n".join(map(str, planes)) + "\n"})

    case("G=1, P=1", 1, [1])
    case("G=1 두 번째에서 중지", 1, [1, 1])
    case("첫 비행기부터 가능한 1번 탑승구", 3, [1, 1, 3])
    case("모두 G번 이하 전부 도킹", 5, [5, 5, 5, 5, 5])
    case("전부 도킹 후 추가 비행기", 5, [5, 5, 5, 5, 5, 5, 1])
    case("오름차순", 6, [1, 2, 3, 4, 5, 6])
    case("중지 후 남은 비행기는 무시", 4, [1, 1, 4, 4, 4])
    for i in range(7):
        g = rng.randint(1, 15)
        p = rng.randint(1, 20)
        case(f"작은 랜덤 {i+1}", g, [rng.randint(1, g) for _ in range(p)])
    G = 100000
    case("최대 G, P 전부 G번 (선형 탐색 최악)", G, [G] * G)
    case("최대 G, P 랜덤", G, [rng.randint(1, G) for _ in range(G)])
    case("최대 G, P 큰 번호 위주", G, [rng.randint(G - 1000, G) for _ in range(G)])
    # 내림차순으로 도킹시켜 긴 사슬을 만든 뒤 맨 위에서 다시 찾기 (재귀 find는 깊이 초과 위험)
    case("최대 G, P 내림차순 후 다시 G번", G, list(range(G, 1, -1)) + [G])
    return cases
