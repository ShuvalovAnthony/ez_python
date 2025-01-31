for n in range(1, 10**12):

    bin_n = bin(n)[2:]

    temp = bin(bin_n.count("1"))[2:] + bin(bin_n.count("0"))[2:]
    r = int(temp, 2)

    if r == 183:
        print(n)
        break