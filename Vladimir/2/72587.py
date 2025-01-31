from itertools import product, permutations

def f(x, y, z, w):
    return (x <= (z <= w)) and (z <= (y == (not w)))


for a in product([0, 1], repeat=6):
    t = [
        (a[0], 0, 0, 0),
        (a[1], a[2], 0 ,0),
        (a[3], a[4], 0, a[5])
    ]

    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(''.join(p))