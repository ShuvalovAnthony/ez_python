from itertools import combinations


def p(x):
    return 15 <= x <= 142


def q(x):
    return 38 <= x <= 167


def a(x, start, stop):
    return start <= x <= stop # НАИМЕНЬШАЯ (наибольшая - <)



coords = combinations(
    sorted([15, 142, 38, 167]), r=2
)


dlini = set()

for start, stop in coords:
    flag = True

    for x in range(10, 180):
        if (
            not (
                q(x) <=
                (
                    (
                        (not a(x, start, stop)) and
                        p(x)
                    ) <=
                    (not q(x))
                )
            )
        ):
            flag = False


    if flag:
        dlini.add(stop - start)


print(min(dlini))