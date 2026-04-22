def to_5(num):
    res = ''

    while num > 0:
        res += str(num%5)
        num //= 5

    return res[::-1]


res = []

for n in range(1, 10000):
    n_5 = to_5(n)

    if n_5[-1] == "0":
        n_5 = n_5.replace("1", "_")
        n_5 = n_5.replace("4", "1")
        n_5 = n_5.replace("_", "4")

        n_5 = '33' + n_5

    else:
        n_5 = "3" + n_5[1:] + "42"

    r = int(n_5, 5)

    if r < 1922:
        res.append([n, r])


res = sorted(res, key=lambda x: (
    -x[1],
    x[0]
))


for row in res:
    print(row)