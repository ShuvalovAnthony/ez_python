ip1 = "151.172.115.121"
ip2 = "151.172.115.156"


bin_ip1 = [bin(int(i))[2:].zfill(8) for i in ip1.split('.')]
bin_ip2 = [bin(int(i))[2:].zfill(8) for i in ip2.split('.')]


print(bin_ip1)
print(bin_ip2)


['10010111', '10101100', '01110011', '0 1111001']
['10010111', '10101100', '01110011', '1 0011100']