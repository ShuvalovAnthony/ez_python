# типы данных
# int, str, float, bool, list, set, tuple, dict

# int
# + - * **
# / // %


# money = 10
# price = 30

# print(money // price)
# print(money % price)


# print(16**0.5)

# 610 = 512 + 64 + 32 + 2

# str - строки/текст/массив символов

# s = "Hello world!!      Lower Upper"

# print(s.lower())
# print(s.upper())
# print(s.lower().count("l"))
# print(s.split())
# print(s.replace("o", "_", 1))
# print(' '.join(["abc", "cde", "def"]))
# print(s.find("o"))
# print("1010".zfill(8))

# print(s[8])
# print(s[-3])


# slices срезы 

# print(list(range(5, 20, 3)))

# s = "0123456789ABCDEF"

# 012345
# 2468A
# FDB9
# 789ABC


# print(s[:6])
# print(s[2:11:2])
# print(s[-1:-8:-2])
# print(s[7:13])

# text = "AaaBbbCcc"
# # text = text[0] + "r" + text[2:]

# print(text)

# bin() oct() hex() - str



# list списки

# nums = [-5, 1, 2, 3, 4, -7, 6, -4, -3]


# print(nums)

# nums[-1] = 0
# nums.append(10)

# print(nums[-1])


# print(nums)

# nums = sorted(nums)

# print(nums)


# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc tellus nieque, pretium id eleifend id, tempus in ante. Vestibulum laoreet, massa mattis laoreet venenatis, eros metus egestas velit"

# посчитать количество уникальных символов

# print(len(set(text)))

# посчитать количество каждого символа

# for symb in sorted(set(text.lower())): # a
#     print(symb, "встречается столько раз:", text.count(symb))

# words = text.lower().split()

# set множество

# nums = {3, 4, 5, 6, 6, 4, 5, 7, 9, 0, 1, 2, 3, 4}
# # print(nums)

# text = "AabfbdbdbshhdseueueueuOOPIfdyyyfsdiuy"


# nums = {-10, 0, 9, 12, 3, 4, -101, -102}
# nums = {1, 2, 3, 4}



# from itertools import product

# for word in product("ABC", repeat=4):
#     print(word[:2])



# bool логический тип
# True False

# > < == != >= <= 

# n = 3

# if n > 5:
#     print("YES")

# if False:
#     print("NO")



# def check(n):
#     return n > 5

# if check(100):
#     print("Yes")


# False 0 '' [] set() {} 

# True -5, 5, 12.432 [1, ] {1, 2, 3}


n = 77


if n > 0:
    print("positive")
elif n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("Error")

# n = 50


# if n < 100:
#     print("< 100")
# elif n < 200:
#     print("< 200")
# elif n < 300:
#     print("< 300")
# elif n < 400:
#     print("< 400")
