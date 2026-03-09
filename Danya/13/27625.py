net = "192.168.0.13"
mask = "255.255.224.0"

bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]

print(bin_net)
print(bin_mask)


['11000000', '10101000', '000 00000', '00001101']
['11111111', '11111111', '111 00000', '00000000']


left = '1100000010101000000'

counter = 0

for i in range(2**13):
    right = bin(i)[2:].zfill(13)
    
    address = left + right

    if address.count('1')%2 == 0:
        counter += 1


print(counter)