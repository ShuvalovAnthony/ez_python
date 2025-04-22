res = []

for n in range(4, 1000):
    bin_n = bin(n)[2:]

    if n%2 == 0:
        bin_n += bin_n[:3]
    else:
        bin_n = '1' + bin_n + '01'

    r = int(bin_n, 2)

    if r > 600:
        res.append(r)


print(min(res))