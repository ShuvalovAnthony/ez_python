from itertools import *


def f1(w, x, y, z):
    return (w == x) and (y <= z)


def f2(w, x, y, z):
    return (w <= x) <= (y == z)



for a in product([0, 1], repeat=5):
    t = [
        (1, a[0], 1, 1),
        (a[1], 1, 0, 0),
        (a[2], 0, 0, a[3])
    ]

    if len(t) == len(set(t)):
        for p in permutations("wxyz"):
            if (
                (
                    [f1(**dict(zip(p, row))) for row in t] == [1, 1, 0]
                ) and
                (
                    [f2(**dict(zip(p, row))) for row in t] == [0, a[4], 0]
                )
            ):
                print(*p)