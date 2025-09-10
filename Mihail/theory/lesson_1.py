# Типы данных - нужны для того, что комп понимал, какой результат будет давать оператор
# операнды - то, над чем производится действие
# оператор - то, что производит действие

# числовой тип данных - int float
# int - целые числа
# float - вещественные числа / числа с плавающей точкой

# основные арифмет действия
# + - * слож, вычит, умнож
# ** возведение в степень (В ТОМ ЧИСЛЕ - дробную для взятия корней)

# print(16**(1/2))
# приоритет действий как в математике

# деление 
# / - обычное
# // - целочисленное
# % - остаток

# float - вещественные - НАШ ВРАГ
# максимально стараемся избегать операций с дробными числами
# результат деление/возведения в степень - всегда float


# строки - str string 🛑🛑🛑🛑 НЕИЗМЕНЯЕМЫЙ ТИП ДАННЫХ !🛑🛑🛑🛑🛑
# строки записываются в кавычках (одинар/двойных неважное, главное чтоб начин и заканч на одни и те же)


# print('Толстой "Война и мир" и \'пример\'')

# строки можно складывать и умножать

# word_1 = "hello "
# word_2 = "world"

# print(word_1 + word_2) # сложение строк - конкатенация
# print(word_1*7)


# Строковые методы

# text = "Apple World Boom Aboba Tun Tun Tun TUn Tun Sahuuur 12345"
# text.upper() # НЕ ИЗМЕНИЛИ СТРОКУ!!!!!!
# text = text.upper() # ИЗМЕНИЛИ СТРОКУ

# print(text)


# print(text.upper()) # верхний регистр
# print(text.lower()) # нижний

# print(text.count("1")) # считает количество ПОДСТРОК в СТРОКЕ substrings
# print(text.find("AB")) # возвращает индекс ПЕРВОГО вхождения ПОДСТРОКИ В СТРОКУ
# print(text.index("A"))


# Задачка посчитать количество букв a в строке

# print(text.lower().count("a")) # chaining цепочка методов

# text = "4623543_23543 23423_4325 4234_ 234234"

# print(text.split("_ ")) # разбиваем строку по разделителю и получаем СПИСОК подстрок
# # по умолчанию разделитель - пробелЫ
# s.split(' ') - разделитель ПРОБЕЛ
# s.split() - разделитель ПРОБЕЛЫ!!!!
# print(text.replace("_", ' ').split())
# words = ['4623543', '23543', '23423', '4325', '4234', '234234']

# print(' '.join(['abc', 'egh', 'afds']))
# text = "Apple World Boom AbobaO Tun Tun Tun TUn Tun Sahuuur 12345"

# print(text.replace("o", "0"))

# print(text.zfill(50)) # дополнить строку слева!!! нулями до n знаков

# индексация строк
# идет с нуля, индекс берется в квадратных скобках

# s = '0123456789ABCDEF'

# print(s[0])
# print(s[len(s) - 1])
# print(s[-1])


# СРЕЗЫ slices
# квадратные скобки, правила как в range()
# разделитель - :

# s = '0123456789ABCDEF'

# 012345
# 456789A
# 23456789ABCDEF
# 6789ABCD
# 369C
# EA
# 05A


# 01234567
# 789ABCD
# ABCDEF
# 2468
# FDB9

# print(s[:8])
# print(s[7:14])
# print(s[7:-2])
# print(s[10:])
# print(s[2:10:2])
# print(s[-1:8:-2])
# print(s[::-1]) # REVERSE STRING/LIST


# # start=0, stop, step=1
# # stop EXCLUDED НЕ ВХОДИТ!!!!!!
# for i in range(5, 10, 2):
#     print(i)


# КОЛЛЕКЦИИ
# коллекции это типы данных по которым можно итерироваться (циклом)

# str
# list - списки
# set - множества
# tuple - кортеж
# dict - словари
# range() - range obj


# list - список
# записывается в квадратных скобках
# может содержать любые типы данных
# 🛑🛑🛑ИЗМЕНЯЕМЫЙ🛑🛑🛑


# nums = [1, 2, 3, 4]

# СПИСКИ МОГУТ содержать разные типы данных
# НО это НЕЖЕЛАТЕЛЬНО

# print(nums[0]) # доступ к элементам списка по индексу осущ также как в строках

# print(nums)

# nums[0] = 5
# nums[-1] = 10

# print(nums)

# a = [1, 2, 3, [0, 0, 0], 8, 8, 8]
# b = a.copy()

# a[0] = 5
# a[3][1] = 4
# b[-1] = 7

# print(a)
# print(b)

# Списковые методы
# nums = [1, 2, 3, 4]

# print(nums.count(1)) # считаем колво элементов
# print(nums.insert(1, 9))
# print(nums.append(0)) # добавить элемент в КОНЕЦ списка
# print(nums[2:])

# print(nums)
# nums.copy() # копируем

# a = [1, 2, 3]
# b = [4, 5, 6]


# b.append(a.pop())

# print(a)
# print(b)

# board = [
#     [11, 12, 13, 14, 15],
#     [21, 22, 23, 24, 25],
#     [31, 32, 33, 34, 35],
#     [41, 42, 43, 44, 45],
#     [51, 52, 53, 54, 55],
# ]


# # 44 55 11 15 51 32 31 54 -> *
# board[1][-1] = "*"



# for row in board: print(*row)


# Множества - записываются в фигурных скобках {}
# и словари записываются в фигурных скобках {}
# 1) множества не имеют
# повторяющихся элементов
# 2) множества неупорядочены

# mnozh = set() # пустое множество создается при помощи конструктора
# nums = []
# # mnozh.add(5) # добавить элемент в множество

# for i in [-5, 8, 9, -13, 19, 189, -177, 555, 666, -432, 12]:
#     mnozh.add(i)
#     nums.append(i)

# print(mnozh, list(mnozh))
# print(nums)




# tuple - КОРТЕЖ
# НЕИЗМЕНЯЕМЫЙ СПИСОК, записывается в скобках

# nums = (1, 2, 3, 4, 5)

# print(nums[0])
# print(nums[2:])
# print(nums.count(3))


# dict - СЛОВАРИ dictionary
# записываются в фигурных скобках
# хранят пары ключ-значение
# key: value


# data = {
#   "ok": True,
#   "result": [
#     {
#       "update_id": 123456789,
#       "message": {
#         "message_id": 123,
#         "from": {
#           "id": 987654321,
#           "is_bot": False,
#           "first_name": "John",
#           "username": "john_doe",
#           "language_code": "en"
#         },
#         "chat": {
#           "id": 987654321,
#           "first_name": "John",
#           "username": "john_doe",
#           "type": "private"
#         },
#         "date": 1678886400,
#         "text": "Hello, world!"
#       }
#     }
#   ]
# }

# print(data["result"][0]["message"]["from"]["id"])

# for student in students:
#     print(student["ID"])

# range(10) - ГЕНЕРАТОР АРИФМЕТИЧЕСКИХ ПРОГРЕССИЙ


# nums = [1]


# for i in range(10):
#     nums.append(nums[-1]*3)

# print(nums)



# ip = "192.168.11.213"

# bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]



# from time import time
# from random import randint
# start = time()

# nums = []


# for i in range(10**6):
#     # print(i)
#     nums.append(randint(-10**10, 10**10))


# # nums = [randint(-10**10, 10**10) for i in range(10**6)]


# print(time() - start)

# циклы, условия и функции