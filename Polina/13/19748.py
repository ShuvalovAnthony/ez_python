ip1 = '157.220.185.237'
ip2 = '157.220.184.230'


bin_ip1 = [bin(int(i))[2:].zfill(8) for i in ip1.split('.')]
bin_ip2 = [bin(int(i))[2:].zfill(8) for i in ip2.split('.')]


print(bin_ip1)
print(bin_ip2)


# ['10011101', '11011100', '10111 00  1', '11101101']
#   11111111    11111111    11111 00  0    00000000
# ['10011101', '11011100', '10111 00  0', '11100110']

counter = 0

for i in range(2**9):
    right = bin(i)[2:]

    if (14 + right.count('1')) == 15:
        counter += 1


print(counter)