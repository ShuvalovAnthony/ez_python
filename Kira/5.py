def to_3(n) -> str:
    res = ''

    while n > 0:
        res += str(n%3)
        n //= 3

    return res[::-1]

res = []

for n in range(166, 10_000):
    n_3 = to_3(n)

    sm_cifr = sum([int(i) for i in n_3])

    if sm_cifr%9 == 0:
        n_3 += '2'
    else:
        n_3 += to_3(sm_cifr%9)

    r = int(n_3, 3)

    res.append(r)

print(min(res))