from itertools import combinations

def p(x):
    return 84 <= x <= 341

def q(x):
    return 198 <= x <= 412

def a(x, start, stop):
    return start <= x <= stop

coords = combinations([84, 198, 341, 412], r=2)

for start, stop in coords:
    flag = True
    for x in range(80, 420):
        if ((not(p(x) == q(x))) and (not(a(x, start, stop)))):
            flag = False
    if flag:
        print(stop - start)