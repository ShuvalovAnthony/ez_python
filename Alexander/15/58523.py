from itertools import combinations


def p(x):
    return 13 <= x <= 31

def q(x):
    return 18 <= x <= 80

def r(x):
    return 48 <= x <= 114

def a(x, start, stop):
    return start <= x <= stop # НАИМ длина отрезка - <=
                            # НАИБ - <


intervals = combinations(
    sorted([13, 31, 18, 80, 48, 114]),
    r=2
)

dlini = []

for start, stop in intervals:
    flag = True

    for x in range(1, 120):
        if not (
            (not (
                q(x) <=
                (p(x) or r(x))
            )) <=
            (
                (not a(x, start, stop)) <=
                (not q(x))
            )
        ):
            flag = False
            break

    if flag:
        dlini.append(stop - start)


print(min(dlini))