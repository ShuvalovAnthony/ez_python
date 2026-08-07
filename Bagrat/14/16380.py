# from string import digits, ascii_uppercase


# alph = digits + ascii_uppercase[:15]


# def to_25(num: int):
#     res = ''

#     while num > 0:
#         res += alph[num%25]
#         num //= 25

#     return res[::-1]


# num = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024


# num_25 = to_25(num)

# counter = 0

# for digit in num_25:
#     if digit in alph[11:]:
#         counter += 1

# print(counter)



# 2 sposob

# num = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024

# counter = 0

# while num > 0:
#     if num%25 > 10:
#         counter += 1
#     num //= 25

# print(counter)