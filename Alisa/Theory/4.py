def to_5(num: str):
    res = ''

    while num > 0:
        res += str(num%5)
        num //= 5

    return res[::-1]

from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

def to_13(num: int):
    res = ''

    while num > 0:
        res += alph[num%13]
        num //= 13

    return res[::-1]



for n in range(1000):
    n_5 = to_5(n)