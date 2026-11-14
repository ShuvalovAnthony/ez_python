def modify(num: int):
    num = str(num)
    num = num[0] + num[-1] + num[-2]
    return int(num)


def f(start, stop):
    if start == stop:
        return 1
    if start > stop:
        return 0

    moves = [
        f(start + 1, stop)
    ]

    # start - трехзначное
    if str(start)[-2] < str(start)[-1]:
        moves.append(
            f(modify(start), stop)
        )

    return sum(moves)


print(
    f(100, 150)
)