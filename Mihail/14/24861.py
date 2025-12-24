from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in range(2, 36):
    for y in range(2, 36):
        y_letter = alph[y]
        x_letter = alph[x]

    
        try:
            num1 = int("13F1" + y_letter, x)
            num2 = int("15" + x_letter + "5" + y_letter, 21)

            exp = num1 + num2
            if exp%32 == 0:
                print(x, y, exp//32)
        except:
            ...


