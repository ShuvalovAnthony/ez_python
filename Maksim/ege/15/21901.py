for a in range(200):
    flag = True

    for x in range(200):
        if not (
            (
                (x&52 != 0) and (x&48 == 0)
            ) <=
            (not (x&a == 0))
        ):
            flag = False
            break

    if flag:
        print(a)
        break