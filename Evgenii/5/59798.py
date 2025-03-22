def to_tri(n):
    tri_n = ""

    while n > 0:
        tri_n += str(n%3)
        n //= 3

    return tri_n[::-1]


for n in range(1, 1000):
    tri_n = to_tri(n)

    if n%3 != 0:
        tri_n += to_tri(n%3*5)

    r = int(tri_n, 3)

    if r > 146:
        print(n)
        break
    