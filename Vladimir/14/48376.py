from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:6]


for x in alph:
    summa = int('8' + x + '834', 16) + int('44' + x + '27', 16)

    if summa%23 == 0:
        print(summa//23)