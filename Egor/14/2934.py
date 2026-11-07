num = (
    6*512**180 +
    7*64**181 +
    3*8**184 +
    5*8**125 - 65)


digits = []

while num > 0:
    digits.append(num%64)
    num //= 64

digits = digits[::-1]

print(digits)