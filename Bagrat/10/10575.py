net_ip = "118.193.24.0"
# mask
ip = "118.193.30.139" # host_ip


bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split('.')]
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]



print(bin_net_ip)
print(bin_ip)

['01110110', '11000001', '00011 000', '00000000']
['01110110', '11000001', '00011 110', '10001011']