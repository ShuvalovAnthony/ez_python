net = "132.214.105.0"
# mask 
ip = "132.214.105.51"


bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]


print(bin_net)
print(bin_ip)