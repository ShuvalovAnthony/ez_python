from itertools import combinations


def p(x): return 15 <= x <= 40

def q(x): return 21 <= x <= 63

def a(x, start, stop): return start <= x <= stop


coords = combinations(
    sorted([15, 40, 21, 63]), 2
)

res = []

for start, stop in coords:
    flag = True

    for x in range(10, 70):
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
        res.append(stop - start)


print(min(res))