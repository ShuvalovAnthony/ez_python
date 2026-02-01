# перевод в СС от 2 до 9 из 10ричной


# def to_7(num: int):
#     res = ''

#     while num > 0: # while num:
#         res += str(num%7)
#         num //= 7
#     # остатки задом наперед пишем
#     return res[::-1]


# print(to_7(1234))



# перевод в СС от 2 до 36 включительно из 10ричной
# пример перевода в 18тиричную

# from string import digits, ascii_uppercase

# alph = digits + ascii_uppercase[:8]


# def to_18(num: int):
#     res = ''

#     while num > 0: # while num:
#         res += alph[num%18]
#         num //= 18
#     # остатки задом наперед пишем
#     return res[::-1]


# print(to_18(1234))