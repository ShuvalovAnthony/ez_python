from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(15_000)

@lru_cache
def f(n):
    if n >= 21:
        return f(n - 8) + 1095
    elif n < 21:
        return 10*(g(n - 7) - 36)


@lru_cache
def g(n):
    if n >= 22560:
        return n/23 + 33
    return g(n + 11) - 4


print(
    f(548)
)


