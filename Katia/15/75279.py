for a in range(20_000):
    flag = True # мы считаем, что выбранный А - окей

    for x in range(20_000):
        if not (
            (
                (x&6280 > 0) or (x&3394 > 0)
            ) <=
            (
                (x&10828 == 0) <= (x&a > 0)
            )
        ):
            flag = False
            break

    if flag:
        print(a)
        break
    