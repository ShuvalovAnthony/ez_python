# Цифра - это просто СИМВОЛ которым записывает число
# Число - это количественная мера (что-то считаем)


# 575 - число

# первая ЦИФРА 5 обозначает число 500 !!!!
# вторая ЦИФРА 7 обозначает число 70
# третья ЦИФРА 5 обозначает число 5



# перевод из 10ой в 22ую

# from string import digits, ascii_uppercase


# num = 42347837534985435

# # 10 цифр + 12 букв = 22 символа
# alph = digits + ascii_uppercase[:12]
# res = ''

# while num > 0:
#     res += alph[num%22]
#     num //= 22

# res = res[::-1]

# print(res)
# # print(int(res, 22))

# summa = 0
# for digit in res:
#     # print(digit, alph.index(digit))
#     if digit in "9ABCDEFGHIJKLMNOP":
#         summa += alph.index(digit)

# print(summa) # 82





# num = 42347837534985435
# summa = 0

# while num > 0:
#     if num%22 > 8:
#         summa += num%22
#     num //= 22

# print(summa) # 82







# СОРТИРОВКА ПО НЕСКОЛЬКИМ ПАРАМЕТРАМ


data = [
    # ID(4), рус(3) мат(2) инф (1)
    # x[0]   x[1] x[2] x[3]
    [2423, 80, 90, 87],
    [1555, 80, 90, 87],
    [3242, 80, 95, 100],
    [5454, 100, 90, 94],
    [1111, 100, 90, 94],
    [5642, 75, 100, 100],
]

data = sorted(data, key=lambda x: [
    -x[3],
    -x[2],
    -x[1],
    x[0]
])



for row in data:
    print(row)