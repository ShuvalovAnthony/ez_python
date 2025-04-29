ip1 = "200.154.190.12"
ip2 = "200.154.184.0"


bin_ip1 = [bin(int(i))[2:].zfill(8) for i in ip1.split('.')]
bin_ip2 = [bin(int(i))[2:].zfill(8) for i in ip2.split('.')]

print(bin_ip1)
print(bin_ip2)



['11001000', '10011010', '1011 1110', '00001100']
['11001000', '10011010', '1011 1000', '00000000']