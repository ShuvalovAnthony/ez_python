mask = "255.192.0.0" # маска
client = "192.168.12.207" # узлы/клиенты/устройства

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]
bin_client = [bin(int(i))[2:].zfill(8) for i in client.split('.')]


print(bin_mask)
print(bin_client)


left = '1100000010'

for i in range(2**22):
    right = bin(i)[2:].zfill(22)

    ip_addr = left + right

    if ip_addr.count('1') == ip_addr.count('0'):
        print(ip_addr)

