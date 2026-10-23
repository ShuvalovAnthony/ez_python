def f(start, stop):
    if start == stop:
        return 1
    elif start > stop:
        return 0

    moves = [
        f(start + 1, stop)
    ]

    if str(start)[-2] < str(start)[-1]:
        moves.append(
            f(
                int(str(start)[0] + str(start)[-1] + str(start)[-2]), stop
            )
        )


    return sum(moves)


print(
    f(100, 150)
)