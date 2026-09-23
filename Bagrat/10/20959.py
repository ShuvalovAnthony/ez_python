net_ip = "203.68.128.0"
mask = "255.255.192.0"

bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split('.')]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]

print(bin_net_ip)
print(bin_mask)


left = "110010110100010010"

# ['11001011', '01000100', '10 000000', '00000000']
# ['11111111', '11111111', '11 000000', '00000000']

# 14 нулей в маске
counter = 0

for i in range(2**14):
    right = bin(i)[2:].zfill(14)

    ip = left + right

    if ip.count("1")%7 != 0:
        counter += 1

print(counter)



