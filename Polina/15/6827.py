from itertools import combinations


def p(x): return 257 <= x <= 1000

def q(x): return 5 <= x <= 100

def r(x): return 99 <= x <= 258

def a(x, start, stop): return start <= x <= stop



intervals = combinations(
    sorted([257, 1000, 5, 100, 99, 258]*2),
    r=2
)


dlini = set()

for start, stop in intervals:
    flag = True

    for x in range(0, 1010):
        if not (
            (a(x, start, stop) <= r(x)) and 
            (
                (
            not (a(x, start, stop) <= p(x))
            ) <=
            q(x)
            )
        ):
            flag = False
            break


    if flag:
        dlini.add(stop - start)


print(min(dlini))