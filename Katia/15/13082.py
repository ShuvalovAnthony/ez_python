for a in range(1,500):
    flag = True
    for x in range(1,500):
        for y in range(1,500):
            if (
                    (3*x + y > 48) or (x > y) or (4*x+y < a)
            ):
                flag = False
    if flag:
        print(a)