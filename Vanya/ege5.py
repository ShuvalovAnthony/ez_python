def toTri(n: int):
    tri_n = ""
    while n > 0:
        tri_n += str(n%3)
        n //= 3
    return tri_n[::-1]


for n in range(1, 10000):
    tri_n = toTri(n)

    if n%3 == 0:
        tri_n = "1" + tri_n + "02"
    else:
        tri_n = tri_n + toTri(n%3*4)

    r = int(tri_n, 3)

    if r < 100:
        print(n)