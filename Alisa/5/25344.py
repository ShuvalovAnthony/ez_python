def to_base(num: int, base: int):
    """base 2 .. 10"""
    res = ''

    while num > 0:
        res += str(num%base)
        num //= base

    return res[::-1]


def sum_cifr(num: int):
    res = 0

    for digit in str(num):
        res += int(digit)

    return res


res = []

for n in range(1, 10_000):
    tri_n = to_base(n, 3)

    if n%3 == 0:
        tri_n += tri_n[-2:]
    else:
        summa_cifr = sum_cifr(n)
        summa_cifr *= 3
        tri_n += to_base(summa_cifr, 3)

    r = int(tri_n, 3)

    if r > 208 and r%2 == 1:
        res.append(r)


print(min(res))


