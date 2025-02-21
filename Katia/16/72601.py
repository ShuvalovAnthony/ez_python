# 1 1 2 3 5 8 13 21 ....
from functools import lru_cache
from sys import setrecursionlimit, set_int_max_str_digits


setrecursionlimit(10000)
set_int_max_str_digits(10**4)


@lru_cache
def f(n):
    if n < 3: return n
    return (n - 1)*f(n - 2)


print((f(2024) - f(2022))//f(2020))