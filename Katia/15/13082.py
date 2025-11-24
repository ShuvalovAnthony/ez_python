for a in range(1,500):
    flag = False

    for x in range(1,500):
        for y in range(1,500):
            if not (
                (3*x + y > 48) or (x > y) or (4*x+y < a)
            ):
                flag = True
                
    if flag:
        print(a)