mask = '255.224.0.0'
ip = '11.92.135.56'

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]


print(bin_mask)
print(bin_ip)


# ['11111111', '111 00000', '00000000', '00000000']
# ['00001011', '010 11100', '10000111', '00111000']

bin_max_ip = ['00001011', '01011111', '11111111', '11111110']


print(*[int(i, 2) for i in bin_max_ip])
