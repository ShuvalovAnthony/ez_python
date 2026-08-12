def del_(n, m):
    return n%m == 0

for a in range(1, 10_000):
    flag = True

    for x in range(1, 10_000):
        if not (
            del_(x, 33) <= (
                (not del_(x, a)) <=
                (not del_(x, 242))
            )
        ):
            flag = False
            break

    if flag:
        print(a)
    