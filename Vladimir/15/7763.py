# <= - наименьшая длина
# < - наибольшая
from itertools import combinations

def p(x): return 5 <= x <= 30

def q(x): return 14 <= x <= 23

def a(x, start, stop): return start < x < stop


coords = combinations(
        sorted([5, 30, 14, 23]*2), 2
    )

# print(list(coords))

otrezki = []


for start, stop in coords: # for A 
    flag = True

    for x in range(0, 40):
        if not (
            ((p(x)) == q(x)) <=
            (not a(x, start, stop))
        ):
            flag = False
            break

    if flag:
        otrezki.append(stop - start)

print(otrezki, max(otrezki))