num = (
    5*1296**2021 -
    4*216**2022 +
    3*36**2023 -
    2*6**2024 - 
    2025
)

count = 0

while num > 0:
    if num%36%2 == 0:
        count += 1
    num //= 36

print(count)






# способ 2
# from string import digits, ascii_uppercase


# alph = digits + ascii_uppercase

# def to_36(num: int):
#     res = ''

#     while num > 0:
#         res += alph[num%36]
#         num //= 36

#     return res[::-1]


# num_36 = to_36(num)

# count = 0

# for digit in num_36:
#     if int(digit, 36)%2 == 0:
#         count += 1

# print(count)

