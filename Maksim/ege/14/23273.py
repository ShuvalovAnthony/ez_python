from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:19]


for x in alph:
    num1 = int("463" + x + "7921", 29)
    num2 = int(f"8241{x}153", 29)

    res = num1 + num2

    if res%28 == 0:
        print(x, res//28)

