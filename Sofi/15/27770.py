def del_(n, m):
    return n%m == 0


for a in range(1, 1000):
    flag = True

    for x in range(1, 1000):
        # условие для flag = False (бракуем A)
        if not (
            del_(x, 21) <= (
                (not del_(x, a)) <=
                (not del_(x, 77))
            )
        ):
            flag = False
            break

    if flag:
        print(a)
    