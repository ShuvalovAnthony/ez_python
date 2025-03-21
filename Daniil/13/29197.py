network = "132.214.105.0"

ip = "132.214.105.51"


bin_network = [bin(int(i))[2:].zfill(8) for i in network.split('.')]
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]


print(bin_network)

print(bin_ip)