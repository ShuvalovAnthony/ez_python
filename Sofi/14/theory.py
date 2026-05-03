from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:17]

def to_27(num):
    res = ''

    while num > 0:
        res += alph[num%27]
        # print(alph[num%27], num%27)
        num //= 27

    return res[::-1]


# print(to_27(1231233124))

# counter = 0

# for digit in to_27(423675426745234523745246727346):
#     if int(digit, 27) > 10:
#         counter += 1

# print(counter)




# exp = 4327842374823428734623674782374
# counter = 0

# while exp > 0:
#     if exp%27 > 10:
#         print(exp%27, alph[exp%27])
#         counter += 1

#     exp //= 27



# из 37ричной в 10ую

num = "ABC893"

