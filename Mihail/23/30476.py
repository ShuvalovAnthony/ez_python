def f(start, stop, counter=0):
    if start == stop and counter == 9:
        return 1
    elif start < stop:
        return 0
    
    moves = [
        f(start - 3, stop, counter + 1),
        f(start - 1, stop, counter + 1),
    ]

    if start%2 == 0:
        moves.append(f(start//2, stop, counter + 1))

    
    return sum(moves)


print(f(33, 12))