for a in range(1000):
    flag = True

    for x in range(1000):
        if not (
            ((x&52 != 0) and (x&48 == 0)) <= (not (x&a == 0))
        ):
            flag = False

    if flag:
        print(a)
        break