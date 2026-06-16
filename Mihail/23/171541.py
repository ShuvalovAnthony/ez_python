def f(start, stop):
    if start == stop:
        return 1
    elif start < stop:
        return 0
    

    moves = [
        f(start - 3, stop)
    ]

    if start >= 10 and (str(start)[1] < str(start)[0]):
        moves.append(
            f(int(str(start)[1])*10 + int(str(start)[0]), stop)
        )

    return sum(moves)


print(f(43, 13))