from string import digits, ascii_lowercase


alph = digits + ascii_lowercase[:8]


for x in alph:
    num = (
        int("11h" + x + '05', 18) +
        int(f"3f{x}54{x}8", 18) +
        int(f"g{x}{x}{x}9", 18)
    )

    if num%14 == 0:
        print(num//14)
        break