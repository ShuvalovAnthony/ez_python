# коллекции

# str, list, tuple, dict, set

# списки list
# список - коллекция любых типов данных
# ИЗМЕНЯЕМЫЙ тип
# в списках можно хранить ЛЮБЫЕ типы данных
# но рекомендуется хранить элементы только одного типа

# nums = [1, 2, 3, 4, 5]

# print(nums[2])

# nums[1] = 7
# print(nums)


# nums = [1, 2, 3, 4, 5, [0, 5, -3]]

# nums_2 = nums.copy()

# nums[-1][1] = "Hello"

# print(nums)
# print(nums_2)
# print('------')
# nums[1] = 9

# print(nums)
# print(nums_2)


# nums = [1, 2, 3, 4, 5, '7',  '7', '7', '7',]
# nums_2 = []
# print(nums.count("7"))
# print(nums.index(3))

# nums.append("Hello")
# nums.insert(3, "_")
# print(nums)


# nums = [-5, 0, -8, 9, 4, -4, 3, 2**2]

# nums = sorted(nums)[::-1]


# for num in nums:
#     nums.sort()
#     print(num)



# set - МАТЕМАТИЧЕСКИЕ множества
# НЕТ ПОВТОРЕНИЙ ЭЛЕМЕНТОВ
# НЕВОЗМОЖНО УПОРЯДОЧИТЬ

# проверить, что в списке нет повторяющихся эл-тов

# if len(spisok) == len(set(spisok)):
#     ...

# nums = {666, 667, 668, 669, 101, 102, }

# # добавить элемент в множество
# nums.add(1)
# print(nums)

# # print(nums)


# tuple - кортеж
# неизменяемый список

# nums = (1, 2, 3, 4, 5)
# print(nums[1])

# nums[1] = 5


# dict - словари

# nums = [5, 8, 9, 0, 4]
# #       0  1  2  3  4


# nums_d = {
#     "age": 5,
#     "money": 8,
#     "fingers": 9,
#     "cars": 0,
#     "candies": 4
# }


# f = open("Stas/Theory/shops.txt")

# sells = {}

# for row in f:
#     row = row.split()
#     shop_id, sold = row[0], int(row[1])

#     if shop_id not in sells:
#         sells[shop_id] = sold
#     else:
#         sells[shop_id] += sold

# print(sells)


# проверка наличия элемента в коллекции (ключ для словаря)

# text = "ABCDEF"


# if "T" not in text:
#     print("YES")



# nums_d = {
#     "age": 5,
#     "money": 8,
#     "fingers": 9,
#     "cars": 0,
#     "candies": 4
# }

# if "cars" in nums_d:
#     print("YES")


# ЦИКЛЫ

# while - цикл с предусловием
# главный недостаток - можно получить бесконечный цикл
# используем, когда мы хотим БЕСКОНЕЧНЫЙ цикл


# a = 0

# while a < 10:
#     print(a)
#     a += 1


# num = 54389537425982345345

# res = ''

# while num > 0:
#     res += str(num%7)
#     num //= 7

# print(res[::-1])


# while True:
#     if a > 5:
#         break
#     if b < 10:
#         break


# цикл for
# for в python - итератор - пробегается по любым КОЛЛЕКЦИЯМ

# range() - ГЕНЕРАТОР арифметических (!) прогрессий


# for i in range(10):
#     print(i)


# вывести все двузначные числа, кратные 7

# for i in range(14, 100, 7):
#     print(i)


# nums_d = {
#     "age": 5,
#     "money": 8,
#     "fingers": 9,
#     "cars": 0,
#     "candies": 4
# }

# for el in nums_d:
#     print(el, nums_d[el])

# for propertie, value in nums_d.items():
#     print(propertie, value)



# marks = {
#     "Ivanov": [1, 2, 3, 4, 1, 2, 3, 4],
#     "Petrov": [1, 3, 5, 6, 7]
# }

# for second_name, student_marks in marks.items():
#     print(second_name, "средний балл", sum(student_marks)/len(student_marks))