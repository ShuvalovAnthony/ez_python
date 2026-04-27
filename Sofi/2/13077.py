from itertools import product, permutations


def f1(x, y, z, w):
    return ((w == x) and (y <= z))

def f2(x, y, z, w):
    return ((w <= x) <= (y == z))


for a in product([0, 1], repeat=7):
    table = [
        (1, a[0], 1, 1),
        (a[1], 1, 0, 0),
        (a[3], 0, 0, a[4])
    ]

    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            if (
    
    ([f1(**dict(zip(p, row))) for row in table] == [1, 1, 0]) and
    ([f2(**dict(zip(p, row))) for row in table] == [0, a[2], 0])
    
            ):
                print(*p)
            
