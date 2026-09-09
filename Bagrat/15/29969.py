for a in range(250):
    flag = True

    for x in range(250):
        for y in range(250):
            if not (
                (x > a) or (y > a) or (x + 2*y < 80)
            ):
                flag = False

    if flag:
        print(a)