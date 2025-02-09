for n in range(1, 10**2):
    bin_n = bin(n)[2:]
    for _ in range(2):
        summa_cifr = bin_n.count("1")
        bin_n += str(summa_cifr%2)

    r = int(bin_n, 2)

    if r > 77:
        print(n)
        break