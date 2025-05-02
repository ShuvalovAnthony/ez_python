ip1 = "123.20.103.136"
ip2 = "123.20.103.151"


bin_ip1 = [bin(int(i))[2:].zfill(8) for i in ip1.split('.')]
bin_ip2 = [bin(int(i))[2:].zfill(8) for i in ip2.split('.')]


print(bin_ip1)
print(bin_ip2)


['01111011', '00010100', '01100111', '1000 1 000']
['01111011', '00010100', '01100111', '1001 0 111']

