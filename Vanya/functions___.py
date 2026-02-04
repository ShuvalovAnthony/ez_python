# функция - абстракция, кусок кода, который можно переиспользовать
# у функции есть параметры - это локальные переменные

# def greetings(name: str):
#     return "Привет " + name + "!"

# перевод из 10ой в СС с основанием от 2 до 9


# def to_5(num: int):
#     res = ''

#     while num: # while num > 0
#         res += str(num%5)
#         num //= 5

#     return res[::-1]

# print(to_5(1234))
# print(int("14414", 5))

# # универсальная функция
# def convert(num: int, to_base: int): #
#     """to_base от 2 до 9"""
#     res = ''

#     while num: # while num > 0
#         res += str(num%to_base)
#         num //= to_base

#     return res[::-1]


# num = int(input("Введите число "))
# to_base = int(input("Введите систему счисления от 2 до 9 "))

# print(f"Результат перевода вашего числа {num} в систему счисления {to_base}:" ,convert(num, to_base)

# функция поиска целых корней квадратного уравнения

# def find_roots(a, b, c):
#     dicriminant = b**2 - 4*a*c
#     if dicriminant > 0:
#         root1 = (-b + dicriminant**0.5)/(2*a)
#         root2 = (-b - dicriminant**0.5)/(2*a)
#         return [root1, root2]
#     elif dicriminant == 0:
#         return -b/(2*a)
#     return "No solution"


# print(find_roots(2, -5, -18))

# def is_triangle(a, b, c):
#     a, b, c = sorted([a, b, c])
#     return a + b > c

# if is_triangle(12, 32, 43):
#     print("Треугольник существует")
# else:
#     print("Треугольник не существует")