from itertools import *

def f(x, y, z, w):
    return (not (y and (not x))) and (not (x == z)) and w


for a in product([0, 1], repeat=4): # repeat = КОЛ-ВО ПРОПУСКОВ
    table = [
        (0, 0, a[0], 1),
        (0, 1, 0, 1),
        (a[1], a[2], 0, a[3])
    ]

    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print(*p)

