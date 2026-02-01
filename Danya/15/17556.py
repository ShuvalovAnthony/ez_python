def del_(n, m):
    return n%m == 0


for a in range(1, 1000):
    flag = True

    for x in range(1, 1000):
        if not (
            (del_(x, a)) or
            (
                (x in range(70, 91)) <=
                (not del_(x, 22))
            )
        ):
            flag = False

    if flag:
        print(a)