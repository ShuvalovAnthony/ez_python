# Перевод из 10ого IP в 2ый


# ip = "192.168.1.35"
# [i for i in ip.split('.')]
# ['192', '168', '1', '35']
# [int(i) for i in ip.split('.')]
# [192, 168, 1, 35]
# [bin(int(i))[2:] for i in ip.split('.')]
# ['11000000', '10101000', '1', '100011']
# [bin(int(i))[2:].zfill(8) for i in ip.split('.')]
# ['11000000', '10101000', '00000001', '00100011']


ip = "192.168.1.35"
mask = "255.255.255.240"
client_ip = ""

bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]

print(bin_ip)
print(bin_mask)




# # из 2ого в 10тичный

# bin_ip = ['11000000', '10101000', '00000001', '00100000']
# ip = '.'.join([str(int(i, 2)) for i in bin_ip])
# print(ip)
