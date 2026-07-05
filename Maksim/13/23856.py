net = "172.95.116.174"
mask = "255.255.192.0"

bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]


print(bin_net)
print(bin_mask)


['10101100', '01011111', '01  110100', '10101110']
['11111111', '11111111', '11  000000', '00000000']

left = "101011000101111101"

for i in range(2**14):
    right = bin(i)[2:].zfill(14)

    ip_addr = left + right

    if ip_addr.count("1")%5 == 0:
        print(ip_addr)
        break

answ = "10101100.01011111.01000000.00001111" # [172, 95, 64, 15]

print(sum([int(i, 2) for i in answ.split(".")]))