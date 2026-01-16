network = '111.233.75.0'
# mask =
ip_adres = '111.233.75.16'
bin_net = [bin(int(i))[2:].zfill(8) for i in network.split('.')]
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip_adres.split('.')]

print(bin_net)
print(bin_ip)
['01101111', '11101001', '01001011', '000 00000']

['11111111', '11111111', '11111111', '000 00000']

['01101111', '11101001', '01001011', '000 10000']


2**8 = 256