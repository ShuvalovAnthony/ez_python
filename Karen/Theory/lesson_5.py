# Функции - куски кода, которые можно выполнять много раз
# (это как маленькие программы в которых можно менять какие-то значения)



# from turtle import *

# # функция создает при помощи ключевого слова def
# def square(side):
#     for _ in range(4):
#         fd(side)
#         rt(90)

# # использование функции это ее вызов (call function)
# square(50)
# square(100)
# square(200)

# done()




# Напишите функцию, которая ищет наименьший нетривиальный делитель числа
# тривиальные делители



# def minDel(num: int):
#     for i in range(2, int(num**0.5) + 1):
#         if num%i == 0:
#             return i
        
#     return False


# простые числа - делятся на 1 и на самих себя (обязательно 2 делителя!!!!)
# 2 3 5 7 11 13 17 23...

# for num in range(2, 100):
#     if minDel(num):
#         print(num, minDel(num))


# Внутри функций мы никогда не используем print()!!!!

# def summa(a, b):
#     print(a + b)


# (summa(5, None))


# def summa(a, b):
#     return a + b

# print(summa(5, summa(10, 20)))


# text = "Apple Banana Grape"
# ban_word = "Banana"

# print(text.replace(ban_word, ''))

# def ban(text: str, banWord: str):
#     return text.replace(banWord, '')



# # print(ban("Apple Banana Grape", "Banana"))

# while True:
#     gdfgdfgdg = input("Vvedite text: ")
#     banWord = input("Vvedite ban word ")

#     print(ban(gdfgdfgdg, banWord))


# Рекурсивные функции
# Числа Фибоначчи
# 1 1 2 3 5 8 13 21 34...
# 1 2 3 4 5 6 7  8  9

# сохранение результатов работы функций называется кэширование

# from functools import lru_cache


# @lru_cache
# def fibo(n: int): # n -номер числа Фибо
#     if n <= 2:
#         return 1
    
#     return fibo(n - 1) + fibo(n - 2)



# for i in range(1, 100000):
#     # print(i, fibo(i))
#     ...

# print("DONE")

# ЛЮБУЮ РЕКУРСИЮ МОЖНО ПЕРЕПИСАТЬ В ЦИКЛ