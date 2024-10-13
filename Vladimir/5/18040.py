for n in range(10**5 - 1, 0, -2):
    bin_n = bin(n)[2:]

    if n%5 == 0:
        bin_n = bin_n[:3] + bin_n
    else:
        bin_n += bin((n%5)*5)[2:]

    r = int(bin_n, 2)

    if r < 313:
        print(n)
        break