from itertools import product, permutations


def f(x, y, z, w):
    return (z <= (not (y <= x))) or w


for a in product([0, 1], repeat=7):
    table = [
        (a[0], 1, a[1], a[2]),
        (a[3], a[4], 0, 0),
        (a[5], 0, 1, a[6])
    ]

    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
                print(*p)