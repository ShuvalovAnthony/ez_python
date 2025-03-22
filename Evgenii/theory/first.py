# типы данных

# int, float - числовой

# + - *
# /
# //
# %


# str - текст/строка/массив символов/ string

text = "Aaaaaaa написал книгу с название \"Name\""

# print(text.upper())
# print(text.lower())

# print(text.count("a"))
# print(text.index("n"))

# words = text.split()
# print(len(words), words)

# print(text.replace("a", "*_*"))

# num = 32

# print(bin(num)[2:].zfill(8))

# print("a".zfill(100))

# s = "0123456789ABCD"
# 12345
# DCBA
# 3579
# CA86

# print(s[1:6])
# print(s[-1:-5:-1])
# print(s[3:10:2])
# print(s[-2:-9:-2])
# print(s[:len(s)//2])


# list списки/массивы/листы

# example = [
#     123,
#     "hello",
#     [123, 1, 5,],
#     True,
#     (4, 3, 2),
#     {1, 2}
# ]

# print(example[2][0])


# nums = [4, -3, 2, 0, 15]

# # print(nums)

# # nums.append(6)
# # nums.insert(1, 7)
# # print(nums)

# # print(nums.count(4))
# nums[1] = 5
# print(nums[1])


# a = [1, 2, 3]
# b = a.copy()
# b[0] = 5
# print(b)
# print(a)


# data = [
#     1, 2, 3, -1, -5, -7
# ]

# for num in data: # 1, 2, 3, -1, -5, -7
#     if num == 2:
#         data = sorted(data)
#     print(num)

# print(sorted(data, reverse=True))

    # рус мат инф
data = [
    [3, 5, 3],
    [1, 2, 3],
    [1, 2, 4],
    [2, 2, 5],
    [1, 5, 3],
    
]

# # второй столбец по убыванию, если равен - третий столбец по убыванию, если равны - первый по возрастанию

# data = sorted(data, key=lambda x:(
#     -x[1],
#     -x[2],
#     x[0]
# ))

# for row in data:
#     print(row)


# tuple - кортеж/неизменяемый список

# nums = (1, 2, 3)
# print(nums[0])
# print(nums)


# set - множества

nums = {1, 2, 3, 3, 3, 3, 5, 6}
# text = "fsdiufbj8uifsdkjgfndfsgudifgdfkjgnllskjdgf"

# for symb in set(text):
#     print(symb, text.count(symb))

# print(nums)

# nums.add(8)
# nums.add(1)

# print(nums)
# from random import randint

# nums2 = {-10, -1000000000000000, 0, 24, 25, 11, 12}

# for n in range(10):
#     k = randint(-10**6, 10**6)
#     nums2.add(k)
#     print(k, nums2)

# print(nums2)

# print(min(nums2), sorted(nums2))

# bool True===1/False===0

# > < >= <= != == -> bool

# counter = 0

# for i in range(123, 12434):
#     counter += i%2 == 0
#     # if i%2 == 0:
#     #     counter += 1

# print(counter)

# or and <= (импликация) not

# if (a < 5) and (b > 3) or (c < 8) and (not (j > 10)):
#     ...

# for el in [
#     -234, 5435.543, 'gdiofdfjgfg', [432], (1, 1, 1), {5, 3}, True, range(10)
# ]:
#     if el:
#         print("True")
#     else:
#         print("False")


# def isPrime(n):
#     ...


# for n in range(10**9, 10**11):
#     # простые, оканчиваются на 3, содержат три тройки
#     if (n%10 == 3) and str(n).count("3") and isPrime(n):
#         ...

# nums = [1, 2, 3, 4, 5]
# while nums:
#     print(nums)
#     nums = nums[1:]

# print(nums)

# collections/iterables/ коллекция/массив

# text = "ijo34rmg"
# nums = [1, 2, 3]
# natural = {1, 2, 3, 4}
# r = range(10)


# # используем индексы когда нам надо иметь в теле цикла доступ к соседям
# # наприме - вывести пары чисел или срезы от i до i + k
# for i in range(len(nums)):
#     print(nums[i])


# print("-"*10)
# # используем, когда нам нужно просто сделать полный 
# # перебор, не сравнивая объекты между собой
# for num in nums:
#     print(num)


# генераторы
# ip = "123.253.13.5"

# bin_ip = [bin(int(block))[2:].zfill(8) for block in ip.split(".") if block[-1] == "3"]


# print(bin_ip)


# f = open("Evgenii/theory/data.txt")

# data = [
#     [int(i) for i in row.split()] for row in f
# ]

# print(data)



# на вход подается текст и буква
# посчитать количество этих букв в этом тексте


# def counter(text: str, letter: str):
#     return text.lower().count(letter.lower())


# print(counter("AaaaAAAaa", "A"))



# def summa(a, b):
#     return a + b

# # 1 + 2 + 3

# print(
#     summa(1, summa(2, 3))
# )


# 1 1 2 3 5 8 13 21 34....
from functools import lru_cache




gfdg = 5


@lru_cache
def fibo(n): # n - НОМЕР числа Фибоначчи
    if n <= 2: return 1
    return fibo(n - 1) + fibo(n - 2)


# for n in range(1, 5000):
#     print(n, 'oe chislo =', fibo(n))



