import sys
from functools import lru_cache

sys.setrecursionlimit(20000)

@lru_cache
def f(n):
    if n <= 3: return n-1
    elif n>3 and n%2 == 0: return f(n-2) + n//2 - f(n-4)
    else: return f(n-1) * n+f(n-2)
print(f(4952) + 2*f(4958) + f(4964))