def del_(n, m):
    return n%m == 0


for a in range(1, 3000):
    flag = True

    for x in range(1, 3000):
        if not (
            del_(x, 21) <= (
                (not del_(x, a)) <=
                (not del_(x, 77))
            )
        ):
            flag = False

    if flag:
        print(a)
