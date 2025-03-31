for a in range(200):
    flag = True

    for x in range(200):
        for y in range(200):
            if not (
                ((x < 10) <= (y > 40)) or
                (not (
                    (y < a) <= (x > a)
                ))
            ):
                flag = False

    if flag:
        print(a)
        break
