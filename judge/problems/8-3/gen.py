def generate(rng):
    ns = [("최소 N=1", 1), ("N=2", 2), ("N=4", 4), ("N=5", 5), ("N=10", 10), ("N=20", 20)]
    for i in range(5):
        ns.append((f"작은 랜덤 {i+1}", rng.randint(6, 30)))
    for i in range(4):
        ns.append((f"큰 랜덤 {i+1}", rng.randint(100, 999)))
    ns += [("N=500", 500), ("N=999", 999), ("최대 N=1000", 1000)]
    return [{"name": a, "input": f"{n}\n"} for a, n in ns]
