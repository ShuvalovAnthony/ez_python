for n in range(1, 1000):
    bin_n = bin(n)[2:]

    if bin_n.count('1')%2 == 0:
        bin_n += '0'
        bin_n = '10' + bin_n[2:]
    else:
        bin_n += '1'
        bin_n = '11' + bin_n[2:]

    r = int(bin_n, 2)

    if r > 480:
        print(n)
        break