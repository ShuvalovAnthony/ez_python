from functools import lru_cache
import sys


sys.setrecursionlimit(15000)


@lru_cache
def f(n):
    if n < 3: return n
    return (n - 1)*f(n - 2)

print((f(2025) - f(2023))//f(2021))