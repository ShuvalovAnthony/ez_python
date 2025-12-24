from itertools import *

dlini = set()

p = range(14, 43)
q = range(25, 97)

coords = combinations(sorted([14, 42, 25, 96]), r = 2)

for start, stop in coords:
    a = range( start, stop + 1)
    flag = True
    for x in range(1, 200):
            if not(
                (((x in p) <= (x in a)) and (x in q)) <= ((x not in a) <= (x in p))
            ):
                flag = False
                break
    if flag:
        dlini.add(stop - start)
print(min(dlini))