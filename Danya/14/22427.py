from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:4]


for x in alph:
    num1 = int("4B3" + x + "1C7", 14)
    num2 = int(f"5{x}G83F7", 17)

    res = num1 + num2

    if res%15 == 0:
        print(res//15)


