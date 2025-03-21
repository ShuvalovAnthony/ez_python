def to_tri(n):
    res = ''
    while n > 0:
        res += str(n%3)
        n //= 3
    return res[::-1]


for n in range(3, 100):
    tri_n = to_tri(n)
    tri_n_2 = tri_n.replace("0", "*").replace("2", "0").replace("*", "2")
    print(tri_n)
    print(tri_n_2)
    print('-'*10)
    dec = int(tri_n_2, 3)
    r = abs(n - dec)

    if r == 1_864_648:
        print(n, dec)
        break