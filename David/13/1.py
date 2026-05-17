ip_addr = "192.168.108.157"
mask = "255.255.255.192"

bin_ip = [bin(int(i))[2:].zfill(8) for i in ip_addr.split('.')]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]


['11000000', '10101000', '01101100', '10   011101']
['11111111', '11111111', '11111111', '11   000000'] # МАСКА


print(int("011101", 2))