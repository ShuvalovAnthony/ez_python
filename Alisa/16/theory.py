# ряд Фибоначчи

# 1 1 2 3 5 8 13 21
# 1 2 3 4 5 6 7  8

from functools import lru_cache


@lru_cache
def fibo(n: int): # n - номер числа Фибо
    if n <= 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


for n in range(1, 10000):
    print(n, 'ое число фибо равно', fibo(n))