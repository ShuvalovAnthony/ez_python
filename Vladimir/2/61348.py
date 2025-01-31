from itertools import product, permutations


def f1(x, y, w, z):
    return (x == y) and (w <= z)

def f2(x, y, w, z):
    return (x <= y) <= (w == z)


for a in product([0, 1], repeat=5):
    t = [
        (1, a[0], 1, 1),
        (0, 1, 0, a[1]),
        (a[3], 0, 0, a[4])
    ]

    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if (
                ([f1(**dict(zip(p,r))) for r in t] == [1, 1, 0]) and
                ([f2(**dict(zip(p, r))) for r in t] == [0, a[2], 0])
            ):
                print(''.join(p))