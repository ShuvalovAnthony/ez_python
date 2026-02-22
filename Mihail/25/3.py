from itertools import combinations


def multiplication(comb):
    res = 1
    for i in comb:
        res *= i

    return res

for i in range(1, 5):
    for comb in combinations([2, 2, 5, 5], r=i):
        print(comb, multiplication(comb))