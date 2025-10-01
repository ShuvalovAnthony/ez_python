from itertools import product, permutations, combinations


# если что-то считаем то

# counter = 0

# for word in product("ABCD", repeat=3):
#     word = ''.join(word)

#     if условие:
#         counter += 1

# print(counter)


# если ищем индекс

# index = 1

# for word in product("ABCD", repeat=3):
#     word = ''.join(word)

#     print(index, word)
#     # if условие:
#     #     counter += 1

#     index += 1

# # print(counter)


# нет одинаковых рядом стоящих четных цифр

# "*7**3*"
#    **

# def check(num: str):
#     for digit in "02468":
#         num = num.replace(digit, "*")

#     return "**" not in num
