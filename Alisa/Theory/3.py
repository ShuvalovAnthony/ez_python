# for 
# while


# if/elif/else


# if num > 5:
#     print("YES")

# 28926
# functions


# функции - это участок кода, который можно переиспользовать
# множественными вызовами в том числе с разными аргументами/параметрами

# функция это рецепт/инструкция к работе

# def greetings(name): # def - define - СОЗДАНИЕ функции
#     return "Hello " + name


# вызов функции - запуск работника


# def isPrime(num):
#     for i in range(2, int(num**0.5) + 1):
#         if num%i == 0:
#             return False
#     return True


# for num in range(1, 1000):
#     prostoe = True

#     for i in range(2, int(num**0.5) + 1):
#         if num%i == 0:
#             prostoe = False
    
#     if prostoe:
#         print(num, "prostoe chislo")



# def to_3(n):
#     tri_n = ''

#     while n > 0:
#         tri_n += str(n%3)
#         n //= 3

#     return tri_n[::-1]

# res = []

# for n in range(1, 1000):
#     tri_n = to_3(n)

#     if n%3 == 0:
#         tri_n += tri_n[-2:]
#     else:
#         sum_cifr = sum([int(i) for i in tri_n])
#         sum_cifr *= 2

#         tri_n += to_3(sum_cifr)

#     r = int(tri_n, 3)

#     if r > 520 and r%2 == 1:
#         res.append(r)

# print(min(res))



# число оканчивается на четную цифру

# ==
# != 
# and or
# > < >= <=

# def check(num): # True/False
#     return num%10%2 == 0
    
# num = 55

# if check(num):
#     print("оканчивается на четную")
# else:
#     print("не оканчивается на четную")



# nums = [1, 2, 3, 1, 2, 3]

# print(len(set(nums)))


# функция которая говорит есть ли в тексте гласные
# def check(text: str):
#     for glas in "aeyuio":
#         if glas in text.lower():
#             return True

#     return False