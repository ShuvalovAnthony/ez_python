for a in range(1176125 - 10, 1176125 + 10):
    flag = True

    for x in range(486):
        for y in range(485*5 + 1):
            if not (
                (x*y < a) or (5*x < y) or (486 <= x)
            ):
                flag = False


    if flag:
        print(a)