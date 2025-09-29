# 0123456789ABCDEF

# ЧИСЛА НЕ МОГУТ НАЧИНАТЬСЯ С НУЛЯ!!!!!!
# в любой сс это правило работает!!!!!


# ЦИФРЫ по своему числовому значению не могут
# превышать СС минус 1


# Если нам нужно перевести число в 17тиричную
# и посчитать кол-во букв G
# классический способ:

# from string import digits, ascii_uppercase


# alph = digits + ascii_uppercase[:7]

# num = 12456324234
# res = ''

# while num > 0:
#     res += alph[num%17]
#     num //= 17

# res = res[::-1]
# print(res.count("G"))


# способ похитрее

num = 12456324234
counter = 0

while num > 0:
    if num%17 == 16:
        counter += 1
    num //= 17

print(counter)