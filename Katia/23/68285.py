def f(start, stop):
    if (start < stop) or (start in (10, 15)):
        return 0
    if start == stop: return 1

    moves = [f(start - 1, stop)]

    if start%2 == 0: 
        moves.append(f(start//2, stop))
    if start%3 == 0:
        moves.append(f(start//3, stop))

    return sum(moves)


print(f(22, 1))