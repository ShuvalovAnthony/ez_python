res = []

for n in range(1, 1000):
    bin_n = bin(n)[2:]

    if n%3 == 0:
        bin_n += bin_n[-3:]
    else:
        bin_n += bin(n%3*3)[2:]

    r = int(bin_n, 2)

    if r > 151:
        res.append(r)

print(min(res))