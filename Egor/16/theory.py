# рекурсия

# Последовательность Фибоначчи
# Первые два элемента - ноль и единица
# Остальные - сумма двух последние

# from functools import lru_cache
# from sys import setrecursionlimit, set_int_max_str_digits

# set_int_max_str_digits(100_000)
# setrecursionlimit(30_000)


# def fibo(n: int): # n - номер элемента фибоначчи
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1

#     return fibo(n - 2) + fibo(n - 1)


# for n in range(1, 100):
#     print(n, "ое число Фибо равно", fibo(n))


# print(4827346234**4233)

# nums = [0, 1]

# for n in range(2, 1000):
#     nums.append(nums[-2] + nums[-1])

# print(nums)
