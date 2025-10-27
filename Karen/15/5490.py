def del_(n, m):
    return n%m == 0


for a in range(-100, 100):
    flag = True

    for x in range(0, 100):
        for y in range(1, 100):
            if not (
                (del_(108, x) <= (not del_(x, y))) or
                (x + y > 80) or
                (a - y > x)
            ):
                flag = False

    if flag:
        print(a)
        break