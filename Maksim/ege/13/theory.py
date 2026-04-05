ip_1 = "192.168.1.13"
mask = "255.255.255.192"


bin_ip_1 = [bin(int(i))[2:].zfill(8) for i in ip_1.split('.')]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]

