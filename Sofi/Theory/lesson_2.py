# циклы

# while - цикл с предусловием

# num = 4378956345

# num_7 = ''

# while num > 0:
#     num_7 += str(num%7)
#     num //= 7

# print(num_7)


# for - (цикл) - итератор - он проходится по коллекциям (str list set tuple dict)

# nums = [1, 2, 3, 4]
# data = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     1,
#     "dfsf",
#     True
# ]
# text = "1234"
# mnozh = {1, 2, 3, 4, 5}
# r = range(1, 31, 5)


# nums = [-5, 7, 2, 0, 14, -15]


# even_counter = 0

# for num in nums:
#     if num%2 == 0:
#         even_counter += 1


# for i in range(len(nums) - 2):
#     pair = [nums[i], nums[i + 1]]
    


# функции - переиспользуемая часть кода/микропрограмма

# from turtle import *


# def drawSquare(side_len: int):
#     for i in range(4):
#         fd(side_len)
#         rt(90)


# def drawRowOfSquares(side_len, num_of_squares):
#     for i in range(num_of_squares):
#         drawSquare(side_len)
#         fd(side_len)


# drawRowOfSquares(40, 10)

# done()




# генераторы


def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    
    return True


nums = [-4, 8, 11, -13, 17, 23, 8, 9, 2, 72, -44, 15]

# вывести список четных
# even_nums = []

# for num in nums:
#     if num%2 == 0:
#         even_nums.append(num)

# even_nums = [num for num in nums if num%2 == 0]
# print(even_nums)

# prime_nums = [num for num in nums if isPrime(abs(num))]

# print(prime_nums)


# squares_nums = [num**2 for num in nums]

# print(squares_nums)

# mod_nums = [str(num) + "!" for num in nums]

# print(mod_nums)

# bin_nums = [bin(abs(num))[2:] for num in nums]

# print(bin_nums)


# ip = "192.168.17.4"
# [i for i in ip.split('.')]
# ['192', '168', '17', '4']
# [int(i) for i in ip.split('.')]
# [192, 168, 17, 4]
# [bin(int(i)) for i in ip.split('.')]
# ['0b11000000', '0b10101000', '0b10001', '0b100']
# [bin(int(i))[2:] for i in ip.split('.')]
# ['11000000', '10101000', '10001', '100']
# [bin(int(i))[2:].zfill(8) for i in ip.split('.')]
# ['11000000', '10101000', '00010001', '00000100']
# '.'.join([bin(int(i))[2:].zfill(8) for i in ip.split('.')])
# '11000000.10101000.00010001.00000100'


# рекурсия - вызов функцией самой себя

# 1 1 2 3 5 8 13 21 34...
# 1 2 3 4 5 6 7  8  9

# from functools import lru_cache
# from sys import setrecursionlimit

# setrecursionlimit(20000)

# @lru_cache
# def fibo(n): # n - НОМЕР числа Фибоначчи 
#     if n <= 2:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)


# for n in range(1, 5000000):
#     print(n, fibo(n))


