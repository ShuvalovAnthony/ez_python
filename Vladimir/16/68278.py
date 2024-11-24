from functools import lru_cache
import sys

sys.setrecursionlimit(30000)

@lru_cache
def f(n):
    if n == 0: return 0
    elif n%2:
        return f(n-1) + 2*n - 1
    else:
        return 4*f(n/2)

for a in range(100):
    for b in range(100):
        if f(a) - f(b) == 1045: print(a - b)

        