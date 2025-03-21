for n in range(1, 100000000):
    bin_n = bin(n)[2:]
    res = bin(bin_n.count("1"))[2:] + bin(bin_n.count("0"))[2:]
    r = int(res, 2)

    if r == 50:
        print(n)
        break