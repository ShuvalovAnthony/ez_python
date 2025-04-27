from itertools import combinations



def p(x):
    return 17 <= x <= 58


def q(x):
     return 29 <= x <= 80


def a(x, start, stop):
     return start <= x <= stop



intervals = combinations(
     sorted([17, 58, 29, 80]),
     2
)


dlini = set()


for start, stop in intervals:
    flag = True

    for x in range(0, 100):
        if not (
            p(x) <=
            (
                ((q(x)) and (not a(x, start, stop))) <=
                (not p(x))
            )
        ):
            flag = False
            break
     

    if flag:
        dlini.add(stop - start)



print(min(dlini))