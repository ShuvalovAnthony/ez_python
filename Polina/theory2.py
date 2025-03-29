# range(1, 14, 3)

# [1, 4, 7, 10, 13]


# collections iterable коллекции/последовательности

# str, list, tuple, set, dict, iter


# text = "Gwgeorkgerg"
# set_ = {7, 0, -4}
# r = range(10, 100, 5)


# nums = [1, 2, 3, 4, 0, 8, 19, 100]



# for i in range(len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#         print(nums[i], nums[j])


# while for

# n = 324324

# res = ""

# while n > 0:
#     res += str(n%3)
#     n //= 3

# res = res[::-1]

# print(res)


# while True:
#     num = int(input())

#     if num == 0:
#         break

#     print(num)



# functions 

# Fibo 
# 1 1 2 3 5 8 13 21 34 ...

from functools import lru_cache



@lru_cache
def fibo(n): # n - НОМЕР числа Фибоначчи
    if n <= 2: return 1
    return fibo(n - 1) + fibo(n - 2)


for i in range(1, 5000):
    print(i, fibo(i))

