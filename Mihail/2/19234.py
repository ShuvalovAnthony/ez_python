from itertools import *

def f(x, y, w, z):
    return (not (((not x) or y) and (not w))) or (not(z and (not(y and w))))


for a in product([0, 1], repeat = 7):
    table = [
        (0, a[0], a[1], 1),
        (a[2], 1, a[3], a[4]),
        (1, 0, a[5], a[6])
    ]

    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
                print(*p)