# перевод из 10ой в систему счисления от 2 до 9

# def to_5(num: int):
#     res = ''

#     while num > 0:
#         res += str(num%5)
#         num //= 5

#     return res[::-1]


# print(to_5(453543))



# перевод из 10ой в систему счисления от 2 до 36 включительно


def to_32(num: int):
    from string import digits, ascii_uppercase

    alph = digits + ascii_uppercase

    res = ''

    while num > 0:
        res += alph[num%32]
        num //= 32

    return res[::-1]


# print(to_32(654567567567))
# print(int("J1JK8S6F", 32))


