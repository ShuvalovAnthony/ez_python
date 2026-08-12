from itertools import product


for a in range(1000):
    flag = True

    for x, y in product(range(1000), repeat=2):
        if not (
            (x + y <= 27) or
            (y <= x - 1) or
            (y >= a)
        ):
            flag = False
            break

    if flag:
        print(a)