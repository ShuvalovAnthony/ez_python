for a in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not (
                (x <= 19) or 
                (y < 2*x + a-50) or 
                (y > 17)
            ):
                flag = False
    if flag:
        print(a)