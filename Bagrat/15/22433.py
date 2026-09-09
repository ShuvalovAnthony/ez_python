for a in range(10_000):
    flag = True

    for x in range(10_000):
        if not (
            ((x&117 != 0) and (x&91 == 0)) <= (not (x&a == 0))
        ):
            flag = False

    if flag:
        print(a)
        break