from itertools import combinations

def p(x):
    return 56 <= x <= 79
def q(x):
    return 63 <= x <= 85
def a(x,start,stop):
    return start <= x <= stop

intervals = combinations(
    sorted([56,79,63,85]),
    r=2
)

dlini = []

for start,stop in intervals:
    flag = True

    for x in range(1,1500):
        if not (
            (not (p(x) <= q(x))) <= ((not q(x)) <= a(x,start,stop))
        ):
            flag = False
            break
    if flag:
        dlini.append(stop - start)

print(min(dlini))