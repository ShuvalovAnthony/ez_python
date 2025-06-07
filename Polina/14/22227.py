alph = "123456789ABCDEFGHIJK"

for x in alph:
    num1 = int(x + "5B" + x + "8", 21)
    num2 = int("H053" + x + "7", 21)
    res = num1 + num2

    if res%12 == 0:
        print(x, res//12)
        break