# net
mask = "255.255.248.0"
ip = "135.12.172.217"



bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]


print(bin_mask)
print(bin_ip)


bin_net = ['10000111', '00001100', '10101000', '00000000']

net = '.'.join([str(int(i, 2)) for i in bin_net])

print(net)