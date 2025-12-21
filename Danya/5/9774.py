def to_3(num):
    res = ''

    while num > 0:
        res += str(num%3)
        num //= 3
    
    return res[::-1]


results = []

for n in range(1, 1000):
    tri_n = to_3(n)

    if n%3 == 0:
        tri_n += tri_n[-2:]
    else:
        tri_n += to_3(n%3*5)

    r = int(tri_n, 3)

    if r > 133:
        results.append(r)

print(min(results))