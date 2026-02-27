net = "98.162.71.64"
client = "98.162.71.94"

bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]
bin_client = [bin(int(i))[2:].zfill(8) for i in client.split('.')]

print(bin_net)
print(bin_client)