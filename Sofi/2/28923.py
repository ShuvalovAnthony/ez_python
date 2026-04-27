from itertools import product, permutations


def f(x, y, z, w):
    return (
        (x and (not z) and (not w)) or 
        (x and (not z) and y)
    )


for a in product([0, 1], repeat=7):
    table = [
        (1, a[0], a[1], a[2]),
        (0, a[3], 1, a[4]),
        (a[5], a[6], 0, 0)
    ]

    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print(*p)
            
