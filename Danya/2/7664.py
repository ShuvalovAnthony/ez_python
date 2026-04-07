from itertools import *

def f(a, b, c, d):
    return ((a and b) == (not c)) and (b <= d)


t = [
    (1, 0, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 1, 1),
    (1, 1, 0, 0)
]

for p in permutations("abcd"):
    if [f(**dict(zip(p, row))) for row in t] == [1, 1, 1, 1]:
        print("OK")