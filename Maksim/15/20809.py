def del_(n, m):
    return n%m == 0


for a in range(1, 500):
    flag = True

    for x in range(1, 500):
        if not (
            del_(x, a) or (
                (x in range(60, 81)) <=
                (not del_(x, 22))
            )
        ):
            flag = False
            break

    if flag:
        print(a)