# 1 1 2 3 5 8 13 21 34 ...

from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10000)


@lru_cache
def f(n):
    if n < 3: return n
    return (n - 1)*f(n - 2)


print(
    (f(2024) - f(2022))//f(2020)
)

f = [0]*2050

for n in range(2050):
    if n < 3: f[n] = n
    else:
        f[n] = (n - 1)*f[n - 2]

print(
    (f[2024] - f[2022])//f[2020]
)