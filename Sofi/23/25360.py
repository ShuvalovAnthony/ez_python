def f(start, stop):
    if start == stop:
        return 1
    elif (start < stop) or (start == 36):
        return 0
    
    moves = [
        f(start - 3, stop),
        f(start - 6, stop),
        f(start//2, stop)
    ]

    return sum(moves)


print(f(86, 53)*f(53, 12))