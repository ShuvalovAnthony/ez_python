from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

# функция перевода в 21ричную СС

def convert(num: str, from_base, to_base):
    num_10 = int(num, from_base)

    res = ''

    while num_10 > 0:
        res += alph[num_10%to_base]
        num_10 //= to_base

    return res[::-1]


print(convert("ABC4234HJI10230", 34, 7))