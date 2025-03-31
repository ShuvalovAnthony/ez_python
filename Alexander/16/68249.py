from functools import lru_cache


@lru_cache
def f(n):
    if n == 0: return 0
    if n%2 == 1: return f(n - 1) + 2*n - 1
    return 4*f(n//2)




for a in range(10**5):
    for b in range(10**5):
        if f(a) - f(b) == 1001:
            print(a - b)