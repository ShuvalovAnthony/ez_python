from itertools import product


for a, b, c in product([2, 3, 5, 7, 11, 13, 17, 19, 23], repeat=3):
    num = 1

    num = num*a*a
    num = num*b*b
    num = num*c

    if num == 180:
        print(a + b + c)