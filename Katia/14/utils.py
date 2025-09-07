# def convert(num, from_base, to_base):
#     from string import digits, ascii_uppercase

#     alph = digits + ascii_uppercase

#     num = int(str(num), from_base)

#     digits = ""

#     while num > 0:
#         digits += str(alph[num%to_base])
#         num //= to_base

#     return digits[::-1]



# print(convert(1242343, 10, 16))







# alph = "0123456789ABCDEF" # 8ричная
#         0123456789 11 13 15
#                   10 12 14

# num = 4567890

# summa_ostatkov = 0

# while num > 0:
#     if num%29 > 9:
#         summa_ostatkov += num%29
#     num //= 8


