def convert(num, from_base, to_base):
    from string import digits, ascii_uppercase

    alph = digits + ascii_uppercase

    num = int(str(num), from_base)

    digits = ""

    while num > 0:
        digits += str(alph[num%to_base])
        num //= to_base

    return digits[::-1]



print(convert(1242343, 10, 16))