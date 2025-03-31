from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(5000)


def f(n):
    if n < 3: return n
    if n >= 3: return (n - 1)*f(n - 2)



print((f(2024) - f(2022))/f(2020))