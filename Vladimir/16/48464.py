from functools import lru_cache
import sys

# sys.setrecursionlimit(37000)

@lru_cache
def f(n):
    if n == 0: return 0
    return f(n - 1) + n


for i in range(10, 28 + 1):
    print(i, f(i)%3 != 0)


print((1542613234 - 765432010)*1/3 + 1)