from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:17]


for x in alph:
    num1 = int('123' + x + '24', 27)
    num2 = int(f'135{x}78', 27)
    res = num1 + num2

    if res%26 == 0:
        print(x, res//26)
