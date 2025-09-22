def to_5(num: int):
    res = ''

    while num > 0:
        res += str(num%5)
        num //= 5

    return res[::-1]


res = []

for n in range(1, 1000):
    pyat = to_5(n)

    if pyat[-1] == "0":
        pyat = pyat.replace('1', '*').replace('4', '1').replace('*', '4')
        pyat = '33' + pyat
    else:
        pyat += '42'
        pyat = '3' + pyat[1:]

    r = int(pyat, 5)

    if r < 1922:
        res.append([n, r])


res = sorted(res, key=lambda x: [
    -x[1],
    x[0]
])

for row in res:
    print(row)

print(res[0][0])