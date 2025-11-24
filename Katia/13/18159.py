network = '205.154.192.0'
# mask = 
ip_ad = '205.154.212.20'

bin_net = [bin(int(i))[2:].zfill(8) for i in network.split('.')]
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip_ad.split('.')]

print(bin_net)
print(bin_ip)

['11001101', '10011010', '11 0  00000', '00000000']
['11111111', '11111111', '11 1  00000', '00000000']
['11001101', '10011010', '11 0  10100', '00010100']