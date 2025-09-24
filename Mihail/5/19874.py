def to_3(n):
    res = ''

    while n > 0:
        res += str(n%3)
        n //= 3

    return res[::-1]

res = []

for n in range(10, 1000):
    tri_n = to_3(n)

    if n%4 == 0:
        tri_n += tri_n[-3:]
    else:
        tri_n = '1' + tri_n + '20'
    
    r = int(tri_n, 3)

    if r > 423:
        res.append(r)


# print(min(res))