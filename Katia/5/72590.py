results = []

for n in range(123_456_789, 456_789_012):
    bin_n = bin(n)[2:]

    if n%2 == 0:
        bin_n = '11' + bin_n
    else:
        bin_n = '1' + bin_n + '10'

    r = int(bin_n, 2)

    results.append(r)

print(max(results))