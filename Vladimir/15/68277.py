for a in range(-100, 100):
    flag = True

    for x in range(-100, 100):
        for y in range(-100, 100):
            if not (
                (
                    (x < 10) <=
                    (y > 40)
                ) or
                (not (
                    (y < a) <=
                    (x > a)
                ))
            ):
                flag = False
    
    if flag: 
        print(a)
        break
    