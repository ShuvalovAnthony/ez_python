net = "222.121.128.0"
mask = "255.255.224.0"


bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]

print(bin_net)
print(bin_mask)


# ['11011110', '01111001', '100 00000', '00000000']
# ['11111111', '11111111', '111 00000', '00000000']

counter = 0

for i in range(2**13):
    ip = bin(i)[2:].zfill(13)
    if ip[-2] == ip[-1]:
        counter += 1

print(counter)