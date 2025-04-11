mask = "255.255.255.192"
ip = "218.194.82.148"


bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]


print(bin_mask)
print(bin_ip)

res = ['11011010', '11000010', '01010010', '10111110']

print([int(i, 2) for i in res])

# 21819482190