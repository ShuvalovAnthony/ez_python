def f(start, stop):
    if start == stop:
        return 1
    
    if (start < stop) or (start == 7):
        return 0
    
    moves = [
        f(start - 1, stop),
        f(start - 4, stop),
        f(start//3, stop)
    ]

    return (
        sum(moves)
    )


print(f(19, 13)*f(13, 2))