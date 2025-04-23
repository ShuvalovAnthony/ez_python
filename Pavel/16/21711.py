from functools import lru_cache
from sys import setrecursionlimit


setrecursionlimit(10000)


def f(n):
    if n < 20: return n
    if n >= 20: return (n - 6)*f(n - 7)



print(
    (f(47872) - 290*f(47865))/f(47858)
)









# @lru_cache
# def fibo(n): # n - номер числа Фибоначчи
#     if n <= 2: return 1
#     return fibo(n - 2) + fibo(n - 1)



# # 1 1 2 3 5 8 13 21 34 ....


# for n in range(1, 5000):
#     print(n, fibo(n))