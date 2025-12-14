def f(start, stop):
    if start == stop: return 1
    elif (start > stop) or (start == 35): return 0

    moves = [
        f(start + 1, stop),
        f(start + 2, stop),
        f(start*2, stop)
    ]

    return sum(moves)


print(f(7, 13)*f(13, 15)*f(15, 51))