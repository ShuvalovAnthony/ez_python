for a in range(1176125 - 20, 1176125 + 20):
    flag = True

    for x in range(486):
        for y in range(5*500):
            if not (
                (x*y < a) or (5*x < y) or (486 <= x)
            ):
                flag = False

    if flag:
        print(a)