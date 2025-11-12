from itertools import combinations

b = range(54, 121)
c = range(78, 152)

dlini = set()

coords = combinations(sorted([54, 120, 78, 151]), r = 2)

for start, stop in coords:
    flag = True
    for x in range(1, 200):
        if not(
                (x in c) <= (((x in b) and (x not in range(start, stop + 1))) <= (x not in c))
        ):
            flag = False
    if flag:
        dlini.add(stop - start)

print(min(dlini))