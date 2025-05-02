def perevod(n):
    res = ''
    
    while n > 0:
        res += str(n%4)
        n //= 4
        
    return res[::-1]


res = []


for n in range(1, 10000):
    chet_n = perevod(n)

    summa_cifr = sum([int(i) for i in chet_n])

    if summa_cifr%3 == 0:
        chet_n = chet_n.replace('0', '1')
        chet_n = chet_n.replace('2', '0')
        chet_n = chet_n.replace('1', '2')

        chet_n = "32" + chet_n
    
    else:
        chet_n += '33'
        chet_n = chet_n[0] + '10' + chet_n[3:]

    r = int(chet_n, 4)

    if r > 320:
        res.append([n, r])

res = sorted(res, key=lambda x:(
    x[1],
    -x[0]
))

for row in res[:20]:
    print(row)