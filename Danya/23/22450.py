def f(start, stop):
    if start == stop: return 1
    elif start < stop: return 0

    moves = [
        f(start - int(str(start)[0]), stop),
        f(start//2, stop)
    ]

    last_digit = start%10

    if last_digit != 0:
        moves.append(f(start - last_digit, stop))
    else:
        moves.append(f(start - 2, stop))

    return sum(moves)


print(f(47, 40)*f(40, 18)*f(18, 14))