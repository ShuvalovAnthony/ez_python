# условия
# if - открытие конструкции, ТОЛЬКО ОДИН

# elif - доп условие
# elif
# elif

# else - безусловная ветка (для всех остальных случаев)


# num = 11


# if num > 10:
#     print(">10")
# if num > 5:
#     print(">5")
# else:
#     print("<= 5")


# циклы

# первый - с предусловие
# while

# k = 0

# while True:
#     if k >= 100: break

#     print(k)

#     k += 1


# for - итератор

# range() - генератор

# написать все кратные 7ми двузначные числа

# for i in range(123456, 10**10, 123456):
#     print(i)


# text = "fgdjgkdjfngldfgkdfg"
# nums = [-5, 4, -12, 9, 0, 7, 12, 18, -6]
# nums_2 = {1, 2, 3, 534, 7567}


# for i in sorted(nums):
#     print(i)

# print(nums)


# Генераторы

# nums = [-5, 4, -12, 9, 0, 7, 12, 18, -6]

# print(
#     []
# )

# f = open("Egor/Theory/data.txt")

# data = [int(i) for i in f if i > 3]

# print(data)



# функции

# def censor(text: str, word: str):
#     return text.lower().replace(word, '')

# text = "Abc abc abc fisdf Gkd jklgndf jgd abc abc abc"

# print(
#     censor(text, "abc")
# )



# from turtle import *


# def brick(side_a, side_b):
#     for _ in range(2):
#         fd(side_a)
#         rt(90)
#         fd(side_b)
#         rt(90)
    

# def row_of_bricks(num_of_bricks, side_a, side_b):
#     for _ in range(num_of_bricks):
#         brick(side_a, side_b)
#         fd(side_a)


# def wall(num_of_rows, num_of_bricks_in_a_row, side_a, side_b):
#     for _ in range(num_of_rows):
#         row_of_bricks(num_of_bricks_in_a_row, side_a, side_b)
#         up()
#         bk(side_a*num_of_bricks_in_a_row)
#         lt(90)
#         fd(side_b)
#         rt(90)
#         down()

# speed(0)

# wall(4, 6, 15, 8)
# wall(8, 12, 20, 5)

# done()


# def summ_2(a, b):
#     return a + b

# print(
#     summ_2(summ_2(5, 6), 7)
# )


def greetings(name: str):
    if "a" in name.lower():
        return "Hello " + name + ". A letter"
    else:
        return "Hello " + name


names = ["Andrey", "Viktor", "Egor", "Kirill", "Sofa", "Anna"]

print(
    [greetings(name) for name in names]
)