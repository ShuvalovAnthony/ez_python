def f(start, stop):
    if start == stop:
        return 1
    if (start < stop) or (start == 28):
        return 0
    
    moves = [
        f(start - 2, stop),
    ]

    if start%2 == 0:
        moves.append(f(start//2, stop))
    else:
        moves.append(f(start - 3, stop))

    return sum(moves)


print(f(98, 1))