# from string import digits, ascii_uppercase

# alph = digits + ascii_uppercase

# print(alph.index("H"))


for p in range(18, 37):
    num = (
        int("22A12E", p) +
        int("2f1391", p) -
        int('1h05d0', p)
    )

    if num%19 == 0:
        print(num//19)