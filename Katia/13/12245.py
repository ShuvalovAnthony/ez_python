network = "192.168.32.48" # сеть
mask = "255.255.255.240" # маска
ip = "" # клиенты


bin_net = [bin(int(i))[2:].zfill(8) for i in network.split(".")]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]

print(bin_net)
print(bin_mask)


left = '1100000010101000001000000011'
counter = 0

# for i in range(1, 2**4 - 1): # ВСЕ АДРЕСА В СЕТИ КОТОРЫЕ МОЖНО НАЗНАЧИТЬ УСТРОЙСТВАМ
for i in range(2**4): # ВСЕ АДРЕСА В СЕТИ
    right = bin(i)[2:].zfill(4)

    ip_addr = left + right

    if ip_addr.count("1")%2 != 0:
        counter += 1

print(counter)
