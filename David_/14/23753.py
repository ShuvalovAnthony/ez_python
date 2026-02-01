from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:19]

for x in alph:
    num1 = int("923" + x + "874", 29)
    num2 = int(f"524{x}6152", 29)

    res = num1 + num2

    if res%28 == 0:
        print(x, res//28)