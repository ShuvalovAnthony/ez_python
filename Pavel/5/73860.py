for n in range(1, 134217743 + 1):
    bin_n = bin(n)[2:]

    r = int(bin(bin_n.count('1'))[2:] + bin(bin_n.count('0'))[2:], 2)
    # print(n, r)
    if r == 183:
        print(n, 'answ')