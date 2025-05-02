# summa_cifr = sum([int(i) for i in STROKA])

for n in range(1, 1000):
    bin_n = bin(n)[2:]

    bin_n += str(bin_n.count('1')%2)
    bin_n += str(bin_n.count('1')%2)

    r = int(bin_n, 2)

    if r > 253:
        print(n)
        break
