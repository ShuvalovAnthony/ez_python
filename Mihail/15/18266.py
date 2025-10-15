for a in range(1, 1000):
    flag = True

    for x in range(1, 1000):
        if not (
            (x&57 == 0) or
            (
                (x&23 == 0) <= 
                (not (x&a == 0))
            )
        ):
            flag = False


    if flag:
        print(a)
        break # тк наименьшее А