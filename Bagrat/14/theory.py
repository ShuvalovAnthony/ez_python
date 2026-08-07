def to_5(num: int):
    res = ''

    while num > 0:
        res += str(num%5)
        num //= 5

    return res[::-1]




from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:7]

def to_17(num: int):
    res = ''

    while num > 0:
        res += alph[num%17]
        num //= 17

    return res[::-1]