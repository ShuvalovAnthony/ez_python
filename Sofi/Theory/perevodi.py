from string import digits, ascii_uppercase


alph = digits + ascii_uppercase
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 01        10 11 12...

# num = 4736593456349768545
# base = 17

# res = []

# while num > 0:
#     res.append(alph[num%base])
#     num //= base

# res = res[::-1]

# print(res)


# # из 10ой в любую от 2ой до 9рой
# def to_3(num):
#     res = ''

#     while num > 0:
#         res += str(num%3)
#         num //= 3

#     return res[::-1]

# print(to_3(3213213))
# # из 10ой в любую от 2ой до 36ричной
# from string import digits, ascii_uppercase

# alph = digits + ascii_uppercase

# def to_33(num):
#     res = ''

#     while num > 0:
#         res += str(alph[num%33])
#         num //= 33

#     return res[::-1]

# print(to_33(3213213))