res = []

for n in range(1, 1000):
    bin_n = bin(n)[2:]

    if bin_n.count('1')%3 == 0:
        bin_n += bin(bin_n.count('1')%5)[2:]
    else:
        bin_n = '1' + bin_n + '10'

    r = int(bin_n, 2)
    
    if r > 89:
        print(n)


print(min(res))