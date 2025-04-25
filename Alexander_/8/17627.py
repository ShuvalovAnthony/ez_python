from itertools import product
count = 0
for x in product('0123456789abcde', repeat=5):
    s = ''.join(x)

    f = 0
    g = 0

    for digit in s:
        if digit == '8':
            f += 1
        elif digit in 'abcde':
            g += 1

    if f == 1 and g >= 2 and (x[0]!='0'):
        count += 1


print(count)