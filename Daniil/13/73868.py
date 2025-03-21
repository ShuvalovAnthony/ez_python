ip_1 = "206.123.209.193"
ip_2 = "206.123.210.118"


bin_ip_1 = [bin(int(i))[2:].zfill(8) for i in ip_1.split(".")]
bin_ip_2 = [bin(int(i))[2:].zfill(8) for i in ip_2.split(".")]

# print(bin_ip_1)
# print(bin_ip_2)


counter = 0

for n in range(2**10):
    left = "1100111001111011110100"
    right = bin(n)[2:].zfill(10)

    if (left + right).count("1") == 15:
        counter += 1

print(counter)