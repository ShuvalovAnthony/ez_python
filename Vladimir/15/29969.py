for a in range(200):
    flag = True

    for x in range(200):
        for y in range(200):
            if not (
                (x > a) or (y > a) or (x + 2*y < 80)
            ):
                flag = False

    if flag:
        print(a)