for x in range(2030, -1, -1):
    num = 7**170 + 7**100 - x

    digits = []

    while num > 0:
        digits.append(num%7)
        num //= 7

    if digits.count(0) == 71:
        print(x)
        break