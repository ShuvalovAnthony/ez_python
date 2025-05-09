def f(s, step=1): # 1p 2v 3p 4v 5p
    if (s == 0) and (step == 3): return 1
    if (
        (s != 0 and step == 3) or
        (s == 0 and step < 3)
    ): return 0

    moves = [
        f(s - 5, step + 1),
        f(s//3, step + 1)
    ]

    if step%2:
        return all(moves)
    return any(moves)


for s in range(1, 100):
    if f(s):
        print(s)


