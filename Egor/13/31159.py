def f(start, stop):
    if start == stop:
        return 1
    if start > stop:
        return 0

    moves = [
        f(start + 1, stop)
    ]

    # start - трехзначное
    if "1" in str(start):
        moves.append(
            f(
                int(str(start).replace("1", "2")), stop)
        )

    return sum(moves)


print(
    f(11, 92)
)