from itertools import combinations

def p(x, j):
    return 107 <= x <= j

def q(x):
    return 285 <= x <= 714

def a(x, start, stop):
    return start <= x <= stop

for j in range(110, 1000):
    dlini = set()

    coords = combinations(sorted([107, 285, 714, j]), r=2)

    for start, stop in coords:
        flag = True

        for x in range(100, 1000):
            if not (
                p(x, j) <= (
                    (q(x) and (not a(x, start, stop))) <=
                    (not p(x, j))
                )
            ):
                flag = False
                break

        if flag:
            dlini.add(stop - start)

    if min(dlini) == 123:
        print(j)