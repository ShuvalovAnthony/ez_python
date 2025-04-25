
mask = '255.255.255.248'
ip = "225.208.14.67"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]


print(bin_mask)
print(bin_ip)