# num = 2*2401**525 + 3*343**524 - 4*49**523 + 5*49**522 - 6*7**521 - 35

# counter = 0

# while num > 0:
#     if num%49 <= 9:
#         counter += 1

#     num //= 49


# print(counter)



num = 2*2401**525 + 3*343**524 - 4*49**523 + 5*49**522 - 6*7**521 - 35

digits = []

while num > 0:
    digits.append(num%49)

    num //= 49

digits = digits[::-1]
print(digits)