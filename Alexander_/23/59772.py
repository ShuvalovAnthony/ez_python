def f(start, stop):
    if (start > stop) or (start in (9, 15)): return 0
    if start == stop: return 1

    moves = [
        f(start + 1, stop),
        f(start + 3, stop),
        f(start*3, stop)
    ]

    return sum(moves)


print(f(3, 18))