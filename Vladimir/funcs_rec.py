# 1 1 2 3 5 8 13 21 34

#  n - номер числа Фибоначчи
from functools import lru_cache

# @lru_cache
def fibo(n):
    if n <= 2: return 1
    return fibo(n - 1) + fibo(n - 2)


for n in range(50):
    print(n, fibo(n))

