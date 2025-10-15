from itertools import combinations


p = range(15, 143)

q = range(38, 167)

coords = combinations(
    sorted([15, 142, 38, 167]), r=2
)


dlini = set()

for start, stop in coords:
    flag = True

    for x in range(10, 180):
        if (
            not (
                (x in q) <=
                (
                    (
                        (not (x in range(start, stop + 1))) and
                        (x in p)
                    ) <=
                    (x not in q) # not x in q
                )
            )
        ):
            flag = False


    if flag:
        dlini.add(stop - start)


print(min(dlini))