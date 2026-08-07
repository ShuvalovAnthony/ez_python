from string import digits, ascii_uppercase


alph = digits + ascii_uppercase[:19]


for x in alph: # x - str
    num = (
        int("923" + x + "874", 29) +
        int(f"524{x}6152", 29)
    )

    if num%28 == 0:
        print(x, num//28)
