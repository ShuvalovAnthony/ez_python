from itertools import combinations


def p(x):
    return 69 <= x <= 91


def q(x):
    return 77 <= x <= 114


def a(x, start, stop):
    return start <= x <= stop


# <= - если НАИМ
# < если НАИБ


intervals = combinations(
    sorted([69, 91, 77, 114]),
    r=2
)


dlini = set()


for start, stop in intervals:
    flag = True


    for x in range(60, 120):
        if not (
            p(x) <= 
            (
                (not (
                    p(x) == q(x)
                )) or
                (
                    q(x) <= a(x, start, stop)
                )
            )
        ):
            flag = False
            break

    if flag:
        dlini.add(stop - start)


print(min(dlini))