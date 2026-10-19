def generate(rng):
    cases = []
    for n in [1, 2, 3, 5, 6, 7, 11, 100]:
        cases.append({"name": f"n={n}", "input": f"{n}\n"})
    for n in sorted(rng.sample(range(12, 900), 6)):
        cases.append({"name": f"랜덤 n={n}", "input": f"{n}\n"})
    for n in [998, 999, 1000]:
        cases.append({"name": f"최대 근처 n={n}", "input": f"{n}\n"})
    return cases
