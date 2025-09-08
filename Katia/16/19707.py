import sys 
from functools import lru_cache
sys.setrecursionlimit(100000)


k = 0


# @lru_cache
def f(n):
    if n<3: return n*4
    elif n >= 3 and n%2 != 0: return n*2
    else: return 5*f(n-2) + n*n


for n in range(1, 550):
    res = f(n)
    if 100 <= res < 1000:
        k += 1

    print(n, res)

print(k)