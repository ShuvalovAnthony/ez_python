from collections import Counter


num = 5*343**8 + 4*49**12 + 7**14 - 98

digits = []

while num > 0:
    digits.append(num%7)
    num //= 7


print(Counter(digits).most_common(1))


# most_common_digit = 0
# counter = 0

# for digit in set(digits):
#     if digits.count(digit) > counter:
#         counter = digits.count(digit)
#         most_common_digit = digit


# print(most_common_digit)

