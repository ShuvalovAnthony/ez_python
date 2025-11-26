from itertools import *


def f(x, y, z):
    return (x == (not y)) or ((not x) == z)


for a in product([0, 1], repeat=6):
    table = [
        (0, a[0], a[1]),
        (a[2], 0, a[3]),
        (a[4], a[5], 1)
    ]


    if len(table) == len(set(table)):
        for p in permutations('xyz'):
            if [f(**dict(zip(p, row))) for row in table] == [0, 1, 0]:
                print(*p)