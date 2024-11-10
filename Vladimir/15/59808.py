for a in range(100, 0, -1):
    flag = True

    for x in range(0, 100):
        for y in range(0, 100):
            if not (
                (x + 2*y > a) or
                (x > 13) or (y < 44)
            ):
                flag = False
    

    if flag:
        print(a)
        break