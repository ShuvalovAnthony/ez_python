for a in range(1000): # 15
    flag = True
    
    for x in range(1000):
        if not (
            (x&29 != 0) <= ((x&17 == 0) <= (x&a != 0))
        ):
            flag = False
            break

    if flag:
        print(a)
        break