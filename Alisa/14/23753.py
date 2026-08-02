from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:19]

# print(alph, len(alph))


for x in alph:
    res = (
        int("923" + x + "874", 29) +
        int(f"524{x}6152", 29)    
    )

    if res%28 == 0:
        print(x, res//28)