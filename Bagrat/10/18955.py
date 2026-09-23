ip_host1 = "200.154.190.12"
ip_host_2 = "200.154.184.0"


bin_ip_host1 = [bin(int(i))[2:].zfill(8) for i in ip_host1.split('.')]
bin_ip_host2 = [bin(int(i))[2:].zfill(8) for i in ip_host_2.split('.')]


print(bin_ip_host1)
print(bin_ip_host2)

['11111111', '11111111', '1111 0000', '00000000']

['11001000', '10011010', '1011 1110', '00001100']
['11001000', '10011010', '1011 1000', '00000000']


