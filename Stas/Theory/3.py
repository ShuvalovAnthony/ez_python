# условные конструкции
# функции


# условная конструкция открывается словом if 
# if - только 1 раз
# elif - сколько угодно раз
# else - только 1 раз - закрывает условную конструкцию


# каждый if закрывает предыдущий


# # Здесь может быть 2 выхода
# if condition1:
#     ...

# if condition2:
#     ...



# # Здесь только 1 выход будет
# if condition1:
#     ...
# elif condition2:
#     ...



# НЕ касается ЕГЭ !!
# else - НЕ используется для единичного условия

# if n%2 == 0:
#     print("chetnoe")
# else:
#     print("nechetnoe")


# if n%2 == 0:
#     print("chetnoe")
# elif n%2 == 1:
#     print("nechetnoe")
# else:
#     print("error")



# функции (в программировании) - кусок кода, который можно переиспользовать


# from turtle import *


# speed(0)

# задача - нарисовать квадрат
# со стороной 100

# for i in range(4):
#     fd(100)
#     rt(90)



# # def (define) + func_name(args)
# def draw_square(side_len: int):
#     for i in range(4):
#         fd(side_len)
#         rt(90)


# draw_square(100)
# draw_square(200)
# draw_square(50)



# нарисовать стену из кирпичей
# 1) функция рисования одного кирпича

# def brick(side_a: int, side_b: int, color):
#     pencolor(color)
#     for i in range(2):
#         fd(side_a)
#         rt(90)
#         fd(side_b)
#         rt(90)


# def row_of_bricks(num_of_bricks, side_a, side_b, color):
#     pencolor(color)
#     for i in range(num_of_bricks):
#         brick(side_a, side_b, color)
#         up()
#         fd(side_a)
#         down()


# def wall(num_of_rows, num_of_bricks_in_row, side_a, side_b, color="red"):
#     pencolor(color)
#     for i in range(num_of_rows):
#         row_of_bricks(num_of_bricks_in_row, side_a, side_b, color)
#         up()
#         bk(num_of_bricks_in_row*side_a)
#         lt(90)
#         fd(side_b)
#         rt(90)
#         down()



# wall(5, 8, 30, 11, "blue")


# done()







# 29956

# def to_base(n, base):
#     tri_n = ''

#     while n > 0:
#         tri_n += str(n%base)
#         n //= base

#     return tri_n[::-1]


# for n in range(1, 1000):
#     tri_n = to_base(n, 9)

#     print(n, tri_n)



# мы не пишем print() внутри функции
# (кроме случаев когда мы что-то тестируем)


# def summa_dvuh(a, b):
#     return a + b

# print(
#     summa_dvuh(
#         summa_dvuh(5, 7),
#         8
# )
# )



# написать функцию, проверяющую кратность на 5
# True/False


# def is_krat_5(n: int):
#     return n%5 == 0

# n = 15

# if is_krat_5(n):
#     print("Kratno 5")
# else:
#     print("Ne kratno 5")





# # if + bool:
# #     ...
# # if True:
# #     действие выполняется
# # else: # False


# if "hello":
#     print("gdfgd")