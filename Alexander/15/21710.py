from itertools import combinations


def b(x):
    return 36 <= x <= 75


def c(x):
    return 60 <= x <= 110


def a(x, start, stop):
    return start <= x <= stop



intervals = combinations(
    sorted([36, 75, 60, 110]), 2
)


dlini = set()


for start, stop in intervals:
    flag = True

    for x in range(30, 120):
        if not (
            (not a(x, start, stop)) <=
            (
                b(x) == c(x)
            )
        ):
            flag = False
            break

    if flag:
        dlini.add(stop - start)


print(dlini)

