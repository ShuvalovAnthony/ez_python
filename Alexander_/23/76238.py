def f(start, stop, canAdd2=True):
    if start > stop: return 0
    if start == stop: return 1

    moves = [
        f(start + 1, stop, True),
        f(start*2, stop, True)
    ]

    if canAdd2:
        moves.append(f(start + 2, stop, False))
    
    return sum(moves)



print(f(2, 22))