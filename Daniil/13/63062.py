ip_1 = "120.91.85.213"
ip_2 = "120.91.89.205"


bin_ip_1 = [bin(int(i))[2:].zfill(8) for i in ip_1.split(".")]
bin_ip_2 = [bin(int(i))[2:].zfill(8) for i in ip_2.split(".")]

print(bin_ip_1)
print(bin_ip_2)