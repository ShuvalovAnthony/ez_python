# условная конструкция

# if/elif/else
    
# if/elif - условные ветки
# else - безусловная (во всех остальных случаях)


# программка светофор


# color = input("Input color ")

# if color == 'red':
#     print("Stop")
# elif color == "yellow":
#     print("Wait")
# else:
#     print("Go")


# нужно число отнести в один из 3х промежутков

# 1 - 33      34 - 67    68 - 100


# num = 12

# if 1 <= num <= 33:
#     print("A")
# elif num <= 67:
#     print("B")
# elif num <= 100:
#     print("C")

# > <= < >= != == and or not 

# True/False



# функции - переиспользуемые участки кода
# def - имя функции (параметры/аргументы)
# print() - внутри функции не используем (кроме случаев когда смотрим ее работу/отладка)

# def sum_of_two_nums(a, b):
#     return a + b


# print(
#     sum_of_two_nums(5, sum_of_two_nums(6, 7))
# )



# в python - не строгая типизация

# def check(nums: list) -> bool:
#     return nums.count(2) == 5



# data = [
#     [],
#     [],
#     []
# ]

# count = 0


# for row in data:
#     count += check(row)


# рекурсивные функции

# Числа Фибоначчи

# первые два числа - единицы
# каждое следующее число - сумма двух предыдущих

# 1 1 2 3 5 8 13 21 34
# 1 2 3 4 5 6 7  8  9

# from functools import lru_cache


# @lru_cache
# def fibo(n): # n - номер числа Фибоначчи
#     if n <= 2:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)



# for n in range(1, 100_000):
#     print("Число Фибо под номером", n, 'равно', fibo(n))

# from sys import setrecursionlimit, set_int_max_str_digits

# set_int_max_str_digits(10**5)
# setrecursionlimit(50_000)

# def f(n):
#     if n == 1:
#         return 1
#     return (n + 1)*f(n - 1) 


# print(
#     (f(42138) + 3*f(42037))//f(42036)
# )

# print(10**4300 + 5**100)