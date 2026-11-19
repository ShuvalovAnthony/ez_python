# Циклы

# while - цикл с предусловием
# минусы - можно легко получить бесконечный цикл
# плюсы - можно легко сделать бесконечный цикл

# a = 1

# while a < 10:
#     a += 100
#     print(a)
#     a -= 100

#     a += 1


# for - цикл (итератор)

# text = "Hello world"
# nums_1 = [1, 2, 3, 4, 5, [1, 2, 3]] # list список
# nums_2 = (1, 2, 3, 4, 5) # tuple кортеж
# nums_3 = {1, 2, 3, 4, 5} # set - множество
# diapazon = range(10)


# for el in range(10):
#     print(el)


nums = [5, 9, 0, 2, 3, 6]


# # проход по индексам - когда нам нужно получать соседей
# for i in range(len(nums)):
#     print(nums[i])


# проход по элементам - когда нам не нужно 
for num in nums:
    print(num, num**2, num**0.5, 2*num)



# nums = [11, 14, 5, -3, 4, -1, 9, 8, 3]

# square_nums = []


# for num in nums:
#     square_nums.append(num**2)

# print(square_nums)



nums = [10, 5, 19, 12, 33, 45, 1, 12]


# for i in range()
