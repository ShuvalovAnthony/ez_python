net = "192.168.1.15"

bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]



bin_ip = "11000000.10111111.11111110.00000000"

print([int(i, 2) for i in bin_ip.split('.')])