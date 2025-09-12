import sys
from functools import lru_cache
sys.setrecursionlimit(2000)


@lru_cache
def f(n):
    if n < 15:
        return 4
    elif n >= 15 and n%3 == 0:
        return f(2*n//3) + n - 1
    else: return f(n-1) + 3

for n in range(0, 3000):
    if f(n) == 251:
        print(n)