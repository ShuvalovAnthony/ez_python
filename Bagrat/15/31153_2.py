from itertools import combinations


b = range(290, 751)
c = range(135, 676)

vars = combinations(
    sorted([290, 750, 135, 675]),
    r=2
    )

dlini = set()

for start, stop in vars:
    a = range(start, stop + 1)

    flag = True

    for x in range(130, 770):
        if not (
            (
                (not x in b) and( x in c)
            ) <=
            (
                (
                    (not x in a) and
                    (x in c)
                ) <=
                (x in b)
            )
        ):
            flag = False

    if flag:
        dlini.add(stop - start)

print(min(dlini))

