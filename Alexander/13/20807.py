net = "172.16.192.0"
mask = "255.255.192.0"
# ip = ""


bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]


# print(bin_net)
# print(bin_mask)

left = 7

counter = 0

for i in range(2**14):
    right = bin(i)[2:].count('1')

    if (left + right)%5 != 0:
        counter += 1

print(counter)
