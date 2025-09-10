# методы списков

# nums = [1, 2, 3, 4]

# print(nums)
# # добавить элемент в конец списка - .append()

# nums.append(9)

# # вставить элемент на i-ое место

# nums.insert(1, 5)

# # посчитать кол-во элементов - .count()
# # номер элемента в списке - .index() наичнаем с 0!!!

# # .copy() - скопировать список
# a = [1, 2, 3]
# b = a # ЭТО НЕ КОПИРУЕТ СПИСОК!!!!!!
# b = a.copy()


# сортируем списки только при помощи функции sorted()

# nums = sorted(nums) # по возрастанию
# nums = sorted(nums, reverse=True) # по убыванию
# nums = sorted(nums)[::-1] # по убыванию
# print(nums)

# методы множеств


# mnozh = {9, 10, -1, 4}

# print(mnozh)

# # добавить в множество
# # mnozh.add(7)
# # mnozh.add(9)


# print(mnozh)


# {} - set()
# {} - dict() DEFAULT

# s = set() # создать пустое множество при помощи конструктора
# spisok = []

# for i in [-100, 43, 5, 0, 11, 17, -19, -38, 0, 25, 24, 27]:
#     spisok.append(i)
#     s.add(i)

# print(spisok)
# print(s)




# человек вводит число от 1 до 10
# если он вводит число от 1 до 3 вкл - пишет 1-3
# если он вводит от 4 до 7 вкл - пишем 4 - 7
# если он вводит от 8 до 10 вкл - пишем 8 - 10


# num = int(input("Vvedite num "))

# if num <= 3:
#     print('1 - 3')
# if num <= 7:
#     print("4 - 7")
# if num <= 10:
#     print("8 - 10")


# if/elif - УСЛОВНАЯ ВЕТКА
# else - БЕЗУСЛОВНАЯ ВЕТКА

# color = input("Vvedite cvet ")

# if color == "red": 
#     print("Stop")
# elif color == "yellow":
#     print("Wait")
# elif color == "green":
#     print("GO")
# else:
#     print("ERROR")



# проверка на кратность

# if n%a == 0:
#     ...

# n кратно a


# УСЛОВИЯ РАБОТАЮТ ТОЛЬКО С 1 значение - ЛОГИЧЕСКИМ - True/False
# if True/False:
#     ....
