net = "203.68.128.0" # сеть
mask = "255.255.192.0" # маска
client = "" # узлы/клиенты/устройства

bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]
# bin_client = [bin(int(i))[2:].zfill(8) for i in client.split('.')]


# print(bin_net)
# print(bin_mask)


left = '110010110100010010'
count = 0

for i in range(2**14):
    right = bin(i)[2:].zfill(14)

    ip_addr = left + right

    if ip_addr.count('1')%7 != 0:
        count += 1

print(count)