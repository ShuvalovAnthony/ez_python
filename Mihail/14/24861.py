from string import digits, ascii_uppercase

alph = digits + ascii_uppercase


for x in range(16, 37):
    for y in range(16, 37):
        num = int("13F1" + str(y), x) + int("15" + str(x) + "5" + str(y), 21)
        if num % 32 == 0:
            print(x, y, num // 32)