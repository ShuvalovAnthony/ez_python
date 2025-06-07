def to4(n):
    res = ''

    while n > 0:
        res += str(n%4)
        n //= 4
    
    return res[::-1]


res = []


for n in range(1, 2000):
    chet = to4(n)

    summa_cifr = sum([int(i) for i in chet])

    if summa_cifr%4 == 0:
        chet = chet.replace('0', '1').replace('3', '0').replace('1', '3')
        chet += '21'
    else:
        chet += '22'
        chet = '11' + chet[2:]

    r = int(chet, 4)

    if r > 200:
        res.append([n, r])


res = sorted(res, key=lambda x:(x[1], x[0]))

print(res[:5])