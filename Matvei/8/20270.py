from itertools import product


counter = 0


def check(num: str):
    for i in '246':
        num = num.replace(i, '0')

    return (
        (num.count('00') >= 2) and
        ('000' not in num)
    )


for num in product('0123456', repeat=5):
    num = ''.join(num)

    if check(num) and (num[0] != '0'):
        counter += 1


print(counter)

