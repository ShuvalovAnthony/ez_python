def f(start, stop, commands=""): # ABABAAAABBBABABBAB
    if start == stop: return 1

    if start < stop: return 0

    moves = []

    if commands[-2:] == "AA":
        if start%2 == 0:
            moves.append(f(start//2, stop, commands + "B"))
        else:
            moves.append(f(start - 7, stop, commands + "B"))
    elif commands[-2:] == "BB":
        moves.append(f(start - 2, stop, commands + "A"))
    else:
        moves.append(f(start - 2, stop, commands + "A"))
        if start%2 == 0:
            moves.append(f(start//2, stop, commands + "B"))
        else:
            moves.append(f(start - 7, stop, commands + "B"))

    return sum(moves)


print(f(40, 1))