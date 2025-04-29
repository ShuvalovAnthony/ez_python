net = "172.16.192.0"
mask = '255.255.192.0'

bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]


print(bin_net)
print(bin_mask)


['10101100', '00010000', '11 000000', '00000000']
['11111111', '11111111', '11 000000', '00000000']

counter = 0

for i in range(2**14):
    right = bin(i)[2:].zfill(14)

    if (7 + right.count('1'))%5 != 0:
        counter += 1

print(counter)

    