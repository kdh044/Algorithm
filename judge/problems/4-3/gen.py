def generate(rng):
    fixed = ["c2", "h8", "a8", "h1", "d4", "e5", "b2", "g7", "a5", "h4", "d1", "e8", "b1", "c3"]
    rest = [c + r for c in "abcdefgh" for r in "12345678" if c + r not in fixed and c + r != "a1"]
    rng.shuffle(rest)
    return [{"name": p, "input": p + "\n"} for p in fixed + rest[:8]]
