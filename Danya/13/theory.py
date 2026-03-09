net = "192.168.0.13"


bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]

print(bin_net)