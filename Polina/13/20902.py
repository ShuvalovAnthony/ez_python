
net = '172.16.80.0'
mask = '255.255.248.0'

bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]

print(bin_net)
print(bin_mask)


['10101100', '00010000', '01010  000', '00000000']
['11111111', '11111111', '11111  000', '00000000']


counter = 0


for i in range(2**11):
    right = bin(i)[2:].zfill(11)

    if (7 + right.count('1'))%2 != 0:
        counter += 1

print(counter)