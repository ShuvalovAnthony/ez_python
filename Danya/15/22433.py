for a in range(1000):
    flag = True

    for x in range(1000):
        if not (
            (x&117 != 0) and (x&91 == 0) <= (not (x&a == 0))
        ):
            flag = False
            break

    if flag:
        print(a)
        break
