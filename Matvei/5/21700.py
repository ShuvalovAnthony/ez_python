def to_tri(n):
    res = ''

    while n > 0:
        res += str(n%3)
        n //= 3

    return res[::-1]


for n in range(3, 10000):
    tri_n = to_tri(n)

    if n%3 == 0:
        tri_n += tri_n[-2:]
    else:
        tri_n += to_tri(n%3*3)

    r = int(tri_n, 3)

    if r <= 130:
        print(n)