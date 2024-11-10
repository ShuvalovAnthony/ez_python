def treug(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c



for a in range(100, 0, -1):
    flag = True

    for x in range(1, 100):
        if not (
            (
                treug(x, 10, 20) <= (
                    (not (max(x, 8) > 24))
                )
            ) ==
            ( not (
                treug(3, a, x)
            ))
        ):
            flag = False
            break

    if flag:
        print(a)
        break

