# Типы данных

# int, float - числовые типы
# int - -5, 0, 15
# float - 1.001, -5.5


# str - string строка/
# list, set, boolean, dict
# + - * / // % ** - оператор
# операнды - то, над чем совершается операция

# 5 + 5 = 10

# "5" + "5" = "55"


# / - обычное деление
# // - целочисленное деление
# % - остаток от деления


# money = 20
# price = 6

# print(money//3)
# print(money%price)

# price(15%17)

# условная конструкция conditions

# if condition_1:
#     ...
# elif 
# elif
# elif

# else:


# циклы
# a = 5
# while a < 10:
#     a += 100 # 105
#     print(a) # 105
#     a -= 100 # 5
#     a += 1 # 6

# нужно вывести все двузначные положительные числа, кратные 14

# for i in range(100): # итератор
#     if (10 <= i <= 99) and (i%14 == 0):
#         print(i)

# for i in range(14, 100, 14):
#     print(i)



# for i in "Hello": # итератор
#     print(i)


from turtle import *


def drawSquare(side_len: int):
    for i in range(4):
        fd(side_len)
        rt(90)


def drawRowOfSquares(side_len: int, num_of_squares: int):
    for i in range(num_of_squares):
        drawSquare(side_len)    
        fd(side_len)


drawRowOfSquares(50, 10)

done()










# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vulputate est vitae purus consequat commodo."

# # 1) Посчитать кол-во гласных в тексте
# # 2) Найти кол-во слов в тексте
# # 3) Убрать все знаки препинания 


# s = "QWERTY56789ASD0123"

# # Получить следующие строки при помощи срезов:
# # QWERTY56
# # 9ASD01
# # 31D
# # WERTY56789ASD012

# print(s...)



# # Дан список чисел - заполнить параметры методов, 
# # чтобы получился следующий список
# nums = [90, 78, 75, 55, 90]
# nums.append()
# nums.append()

# # [90, 78, 75, 55, 90, 12, 34]

# # Отсортировать список по возрастанию


# # Имеется список покупок
# basket = ["apple", "banana", "orange", "apple", "kiwi", "banana", "banana"]

# # Выведи количество (!) уникальных фруктов в корзине
# # Добавь в этот список "pineapple" и удали из списка дубли (конечный тип данных - list)




# # Вывести 1ую, 2ую, 3юю цифры трехзначного числа не 
# # используя строки, а только математические операции
# num = 587