from itertools import combinations

def p(x):
    return 25 <= x <= 64
def q(x):
    return 40 <= x <= 115

def a(x, start, stop):
    return start <= x <= stop 


otrezki = combinations(
    sorted([25, 62, 40, 115]), r = 2
)

dlini = set()
for start, stop in otrezki:
    flag = True

    for x in range(20, 150):
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

    if flag:
        dlini.add(stop-start)

print(min(dlini))