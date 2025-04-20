from itertools import product
from string import ascii_uppercase, digits


alph = digits + ascii_uppercase

results = set()

for x, y in product(range(0, 37), range(9, 37)):
    try:
        num1 = int('5' + alph[x] + alph[y] + "A", 18)
        num2 = int('18' + alph[x] + '7', y)
        summa = num1 + num2
        results.add(summa)

    except:
        ...

print(len(results))


d = set()

for x in range(18):
    for y in range(9, 18):
        if x < y:
            num1 = 5*18**3 + x*18**2 + y*18 + 10
            num2 = 1*y**3 + 8*y**2 + x*y + 7
            res = num1 + num2
            d.add(res)
            

print(len(d))


print(results.difference(d))