mask = "255.255.252.0" # маска
client = "95.24.20.25" # узлы/клиенты/устройства

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]
bin_client = [bin(int(i))[2:].zfill(8) for i in client.split('.')]


print(bin_mask)
print(bin_client)
