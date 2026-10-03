# ‼️‼️‼️ ЧИСЛО В ЛЮБОЙ СС КРОМЕ 10ричной ВСЕГДА В STR ‼️‼️‼️

# 1) переводы ИЗ десятичной системы счисления (СС)
num = 4234
# 1.1) В двоичную/восьмиричную/16тиричную
# bin_num = bin(num)[2:]
# oct_num = oct(num)[2:]
# hex_num = hex(num)[2:]

# 1.2) В любую СС от 2 до 9 включительно

# def to_3(num):
#     res = ''

#     while num > 0:
#         res += str(num%3) # res = res + str(num%3)
#         num //= 3

#     return res[::-1]

# print(to_3(num))


# 1.3) В любую СС от 2 до 36 включительно

# from string import digits, ascii_uppercase

# alph = digits + ascii_uppercase[:7]

# # функция перевода в 21ричную СС

# def to_17(num: int):
#     res = ''

#     while num > 0:
#         res += alph[num%17]
#         num //= 17

#     return res[::-1]


# print(to_17(num))




