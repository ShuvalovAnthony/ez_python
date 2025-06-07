from itertools import combinations


def p(x):
    return 84 <= x <= 341

def q(x):
    return 198 <= x <= 412

def a(x, start, stop):
    return start <= x <= stop


coords = combinations(
    sorted([84, 341, 198, 412]),
    r=2
)


dlini = set()


for start, stop in coords:
    flag = True

    for x in range(80, 450):
        if (
            (not (
                p(x) == q(x)
            )) and
            (not a(x, start, stop))
        ):
            flag = False
            break

    if flag:
        dlini.add(stop - start)


print(min(dlini))