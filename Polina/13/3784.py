mask = '255.255.252.0'
ip = '226.185.90.162'

bin_mask =[bin(int(i))[2:].zfill(8) for i in mask.split('.')]
bin_ip =[bin(int(i))[2:].zfill(8) for i in ip.split('.')]


print(bin_mask)
print(bin_ip)


r = '1010100010'

index = 1


for i in range(1, 2**10 - 1):
    right = bin(i)[2:].zfill(10)

    if r == right:
        print(index)

    index += 1