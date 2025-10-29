net = "205.154.192.0"
# mask
client = "205.154.212.20"


bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]
bin_client = [bin(int(i))[2:].zfill(8) for i in client.split('.')]


print(bin_net)
print(bin_client)
