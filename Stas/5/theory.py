# Перевод из 10ой в любую СС от 2 до 9 включительно

def to_5(num):
    res = ''

    while num > 0:
        res += str(num%5)
        num //= 5 # num = num//5

    return res[::-1]




# Перевод из 10ой в любую СС от 2 до 36 включительно

from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:15]


def to_25(num):
    res = ''

    while num > 0:
        res += alph[num%25]
        num //= 25

    return res[::-1]




# from string import digits, ascii_uppercase

# alph = digits + ascii_uppercase


# def convert(num, base):
#     res = ''

#     while num > 0:
#         res += alph[num%base]
#         num //= base

#     return res[::-1]


# for base in range(2, 37):
#     print("число 4532768435 в системе счисления", base, "выглядит как", convert(4532768435, base))



# convert(123424, 17)


# convert(213234, 16)


# convert(4234234, 5)