from itertools import product


for a in range(-100, 100):
    flag = True

    for x, y in product(range(-100, 100), range(-100, 100)):
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
            break

    if flag:
        print(a)
        break