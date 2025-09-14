# циклы, условия и функции

# Цикл while - цикл с предусловием
# a = 1

# while a <= 20:
#     a += 100
#     print(a)
#     a -= 100

#     a += 1

# Цикл for - итерируется (проходит) по коллекциям

# for num in range(100):
#     print(num)


# Найти все трехзначные числа, кратные 777777

# for num in range(10000656666, 5*10**10, 777777):
#     print(num)


# Условная конструкция
# Дают на вход число от 1 до 100
# num = int(input("vvedite chislo: "))

# if num <= 10:
#     print('1 - 10')
# elif num <= 20:
#     print('2 - 20')
# elif ...:
#     ...
# elif ...:
#     ...


# if ...:
#     ...
# if ...:
#     ...
# if ...:
#     ...
# if ...:
#     ...



# if True/False:
#     ...

# num = 17
# if True:


# False то же самое что и '', [], set(), {}, 0, None
# True - любое число, и ненулевые коллекции

# deliteli = [1, 2]

# if deliteli:
#     print(min(deliteli))


# если в тексте есть гласная найдите длину текста


# для того, чтобы проверить что буква есть в строке, элемент в списке или число в диапазон, а также
# ключ в словаре оператор in

# def check(text: str):
#     for glas in "aeyuio":
#         if glas in text.lower():
#             return len(text)
    
#     return False


# res = check("ahiudashdisad")
# if res:
#     print(res)


# Функции 



# def remove_word_from_text(word: str, text: str):
#     return text.replace(word, '')


# print(remove_word_from_text("aboba", "aboba go to school"))


# def summa(a: int, b: int):
#     return a + b


# рекурсия

# Число Фибоначчи - последовательность начинающ с 1 и 1 и потом
# каждый следующий член послед равен сумме предыдущих двух

# 1 1 2 3 5 8 13...

# напишите функцию которая возвращает n-ое число Фибо
# from sys import setrecursionlimit, set_int_max_str_digits
# # from functools import lru_cache

# setrecursionlimit(20000)


# @lru_cache
# def fibo(n):
#     if n <= 2: return 1

#     return fibo(n - 1) + fibo(n - 2)
    

# for i in range(1, 100000):
#     print(i, fibo(i))


# ЛЮБУЮ рекурсию можно переписать в ЦИКЛ!!!!


# f = [0]*21000

# for n in range(21000):
#     if n < 6:
#         f[n] = n
#     else:
#         f[n] = (3*n - 2) * f[n - 5]

# print(f[:50])


# print(
#     (f[20568] - 51702*f[20563])/f[20553]
# )