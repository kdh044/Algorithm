def generate(rng):
    cases = []

    def case(name, nums, dirs):
        lines = []
        for r in range(4):
            lines.append(" ".join(f"{nums[r * 4 + c]} {dirs[r * 4 + c]}" for c in range(4)))
        cases.append({"name": name, "input": "\n".join(lines) + "\n"})

    seq = list(range(1, 17))
    case("번호 순서대로, 전부 →", seq, [7] * 16)
    case("번호 순서대로, 전부 ↘", seq, [6] * 16)
    case("역순, 전부 ↑ (상어가 바로 갇힘)", seq[::-1], [1] * 16)
    case("16번이 (0,0), 전부 ←", [16] + list(range(1, 16)), [3] * 16)
    case("모든 방향 순환", seq, [(i % 8) + 1 for i in range(16)])
    for i in range(17):
        nums = seq[:]
        rng.shuffle(nums)
        dirs = [rng.randint(1, 8) for _ in range(16)]
        case(f"랜덤 {i+1}", nums, dirs)
    return cases
