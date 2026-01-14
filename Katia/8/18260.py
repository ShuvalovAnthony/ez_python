from itertools import * 
k = 0 
for num in product('0123456789AB', repeat=6):
    num = ''.join(num)

    if num.count('B') == 1 and num[0]!='0':
        for i in '13579B':
            num = num.replace(i, '!')
        for i in '02468A':
            num = num.replace(i, '_')
        if num.count('!') == num.count('_'):
            k += 1

print(k)