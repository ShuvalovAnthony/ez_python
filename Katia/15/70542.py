from itertools import combinations


def p(x):
    return 15 <= x <= 40


def q(x):
    return 21 <= x <= 63


def a(x, start, stop):
    return start <= x <= stop # НАИБ - строго <



intervals = combinations(
    sorted([15, 40, 21, 63]),
    r=2
)

dlini = set()


for start, stop in intervals:
    flag = True

    for x in range(10, 100):
        if not (
            p(x) <=
            (
                (
                    q(x) and (not a(x, start, stop))
                ) <=
                (not p(x))
            )
        ):
            flag = False
            break

    if flag:
        dlini.add(stop - start)

print(min(dlini))