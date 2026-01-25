from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for p in range(2, 100):
    for x in range(1, 500_001):
        num1 = 2*p**3 + 9*p**2 + alph.index("A")*p + 1
        num2 = 4*p**4 + 7*p**3 + 7*p**2 + 7*p**1 + 1
        num3 = 1*p**2 + 2*p + alph.index("A")
        left = num1 + num2 + num3
        right = 10**6 + x

        if left == right:
            print(p)
        


