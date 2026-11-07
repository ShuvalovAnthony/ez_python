from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:13]

for x in alph:
    exp = (
        int(f"81{x}9982", 23) +
        int(f"36{x}24", 23) +
        int(f"72{x}5", 23)
    ) # int число в 10ричной

    if exp%22 == 0:
        print(x, exp//22)
        break


