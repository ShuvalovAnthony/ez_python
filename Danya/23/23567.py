def f(start, stop):
    if start == stop:
        return 1
    elif start < stop:
        return 0
    
    moves = [
        f(start - 2, stop),
        f(start//2, stop)
    ]

    return sum(moves)


print(f(48, 16)*f(16, 2))