from itertools import combinations

def b(x):
    return 290 <= x <= 750

def c(x):
    return 135 <= x <= 675

def a(x, start, stop):
    return start <= x <= stop


vars = combinations(
    sorted([290, 750, 135, 675]), r=2
)


dlini = set()


for start, stop in vars:
    flag = True

    for x in range(130, 770):
        if not (
            (
                (not b(x)) and c(x)
            ) <=
            (
                (
                    (not a(x, start, stop)) and
                    (c(x))
                ) <=
                b(x)
            )
        ):
            flag = False
            break

    if flag:
        dlini.add(stop - start)

print(min(dlini))