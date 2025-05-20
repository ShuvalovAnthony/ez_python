from string import digits, ascii_uppercase

alph = digits + ascii_uppercase


for x in range(1, 37):
    num1 = x*37**4 + 10*37**3 + 13*37**2 + 17*37 + 6
    num2 = 15*39**3 + 3*39**2 + 4*39 + x
    res = num1 + num2

    if res%8 == 0:
        print(res//8)