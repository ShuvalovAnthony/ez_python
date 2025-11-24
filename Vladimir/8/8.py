from itertools import product

alph = '0123456'


def check(num: str):
    for chet in '246':
        num = num.replace(chet, '0')
    for nechet in '35':
        num = num.replace(nechet, '1')

    return num.count("01") == 2


counter = 0

for num in product(alph, repeat=7):
    num = ''.join(num)

    if num[0] != '0' and check(num):
        counter += 1


print(counter)