from itertools import *

def f(x, y, w, z):
    return ((w <= z) == (x <= (not y))) and (x and z)


for a in product([0, 1], repeat=2):
    t = [
        (1, 0, 0, 1),
        (1, 1, 1, 0),
        (0, a[0], 0, a[1])
    ]

    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 0, 1]:
                print(*p)