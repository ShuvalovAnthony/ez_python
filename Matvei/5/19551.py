def tri(n):
    res = ''
    while n > 0:
        res += str(n%3)
        n //= 3

    return res[::-1]


for n in range(1, 1000): # натуральное n !!! >= 1
    tri_n = tri(n)
    
    tri_n = tri_n.replace('2', '_') # 1 раз не надо, меняем сразу все
    tri_n = tri_n.replace('0', '2')
    tri_n = tri_n.replace('_', '0')

    r = int(tri_n, 3)

    if n - r == 378:
        print(n)


