for n in range(1, 10_000):
    bin_n = bin(n)[2:] # bin - 2 oct - 8 hex - 16 + срез ВСЕГДА [2:]

    if n%3 == 0:
        bin_n += bin_n[-3:]
    else:
        bin_n += bin(n%3*3)[2:]

    r = int(bin_n, 2)


    if abs(130 - r) == 3:
        print(n)




