for a in range(100):
    flag = True

    for x in range(1, 100):
        for y in range(1, 100):
            if not (
                (x + y <= 32) or (y <= x + 4) or (y >= a)
            ):
                flag = False

    if flag:
        print(a)
        

