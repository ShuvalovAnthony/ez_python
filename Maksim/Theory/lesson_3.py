# Циклы
# while - цикл с предусловием

# for - итератор (цикл итератор)


# fruits = ["orange", "apple", "grape", "lemon"]


# итерация по индексам
# используется, если нам надо взаимодействовать с соседями/индексами
# for i in range(len(fruits)):
#     fruit = fruits[i]

#     print(fruit, i)


# итерация по объектам
# используется, если нам не надо взаимодействовать с соседями/индексами
# for fruit in fruits:
#     print(fruit)



# lenta = ["g", "y", "r", "g", "y", "r", "g", "y", "r", "g", "y", "r", "g", "y", "r", "g", "r", "y", "g", "y", "r", "g", "y", "r", ]


# def check(troika: list):
#     return troika == ["g", "y", "r"]


# for i in range(0, len(lenta) - 2, 3):
#     troika = lenta[i:i + 3]

#     if not check(troika):
#         print(troika)




# massi_arbuzov = [5, 8, 9, 10, 4, 7, 8, 6, 6, 5, 3, 19]

# for massa_arbuza in massi_arbuzov: # синтаксический сахар
#     if (massa_arbuza < 5) or (massa_arbuza > 10):
#         print("brak")



# from time import time
# from random import randint

# start = time()

# num = 2

# num <<= 4999

# # nums = []


# # for i in range(10**7): nums.append(randint(-10**6, 10**6))


# # nums = [
# #     randint(-10**6, 10**6) for i in range(10**7)
# #     ]

# print(num)

# print(time() - start)
