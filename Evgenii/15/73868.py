ip1 = "206.123.209.193"
ip2 = "206.123.210.118"

bin_ip1 = [bin(int(i))[2:].zfill(8) for i in ip1.split('.')]
bin_ip2 = [bin(int(i))[2:].zfill(8) for i in ip2.split('.')]


# print(bin_ip1)
# print(bin_ip2)
