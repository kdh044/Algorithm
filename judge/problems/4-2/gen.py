def generate(rng):
    # 가능한 입력이 24가지뿐이므로 예제(N=5)를 제외한 전부
    return [{"name": f"N={h}", "input": f"{h}\n"} for h in range(24) if h != 5]
