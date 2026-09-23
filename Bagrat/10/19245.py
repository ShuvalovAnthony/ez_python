mask = "255.255.255.192"
ip = "218.194.82.148" # host_ip


bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]



print(bin_mask)
print(bin_ip)


['11111111', '11111111', '11111111', '11 000000']
['11011010', '11000010', '01010010', '10 111110']