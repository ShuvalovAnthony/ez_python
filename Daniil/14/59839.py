from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:12]


for x in alph:
    res = int("63" + x + "59685", 22) + int(f"17{x}53", 22) + \
    int(f"36{x}5", 22)

    if res%21 == 0:
        print(res//21)
        break