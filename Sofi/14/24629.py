# 1 sposob

# from string import digits, ascii_uppercase

# alph = digits + ascii_uppercase[:4]

# def to_14(num):
#     res = ''

#     while num > 0:
#         res += alph[num%14]
#         num //= 14

#     return res[::-1]


# exp = 14**1402 + 28**501 - 14**51 - 1400


# exp_14 = to_14(exp)

# print(exp_14.count("C"))




# 2 sposob

exp = 14**1402 + 28**501 - 14**51 - 1400

counter = 0

while exp > 0:
    if exp%14 == 12:
        counter += 1

    exp //= 14


print(counter)