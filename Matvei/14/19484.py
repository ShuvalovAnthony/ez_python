num = 5*729**2024 + 3*243**1413 - 7*81**169 - 2*9**107 + 3017

digits = []

while num > 0:
    digits.append(num%27)
    num //= 27



# summ = 0

# for digit in digits:
#     if (digit%2 == 0) and (digit <= 25): summ += digit

# print(summ)


print(sum([i for i in digits if i%2 == 0 and i <= 25]))