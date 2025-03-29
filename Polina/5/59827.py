def to_tri(n):
    tri_n = ""
    while n > 0:
        tri_n += str(n%3)
        n //= 3
    return tri_n[::-1]


results = []

for n in range(1, 10000):
    tri_n = to_tri(n)

    if n%3 == 0:
        tri_n += tri_n[-2:]
    else:
        tri_n += to_tri(n%3*5)

    r = int(tri_n, 3)

    if r <= 173:
        results.append(r)

print(max(results))