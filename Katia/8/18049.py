from itertools import *
k = 0
for num in product('012345678', repeat=7):
    num = ''.join(num)
    if (num[0] not in '0246') and (len(set(num[-3:])) != 1):
        k += 1 
print(k)