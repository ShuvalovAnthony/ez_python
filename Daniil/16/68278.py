from sys import setrecursionlimit
from functools import lru_cache


@lru_cache
def f(n):
    if n == 0: return 0
    if n%2: return f(n - 1) + 2*n - 1
    return 4*f(n/2)


res = []

for a in range(1000):
    for b in range(1000):
        if f(a) - f(b) == 1045:
            res.append(a - b)

print(max(res))