from sys import setrecursionlimit
from functools import lru_cache


@lru_cache
def f(n):
    if n < 10: return n
    if n in range(10, 1000): return f(n//10) + f(n%10)
    return f(n//1000) - f(n%1000)



counter = 0

for n in range(10**6):
    if f(n) == 0: counter += 1

print(counter)