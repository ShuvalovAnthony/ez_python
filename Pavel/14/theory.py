# Перевод в любую систему счисления из 10тичной

# 1 - в СС до 10ой

# num = 5435345345

# res = ''
# base = 3

# while num > 0:
#     res += str(num%base)
#     num //= base

# res = res[::-1]

# print(res)



# 2 - в любую СС до 36ой включительно
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

num = 15626**16 - 3125**3 * 25**19 + 625**4

res = ''
base = 25

while num > 0:
    res += alph[num%base]
    num //= base

res = res[::-1]

print(res)
print(res.count('0'))

# bin()[2:] oct()[2:] hex()[2:]

# print(bin(123)[2:]) # 10->2
# print(oct(123)[2:]) # 10 -> 8
# print(hex(123)[2:]) # 10 - 16


# Из любой до 36ой включительно в десятичную
# число пишется в кавычках!!! основание ИЗ какой системы - после числа
# через запятую. По умолчанию (если ничего не пишешь) - 10
# print(int("12345"))


