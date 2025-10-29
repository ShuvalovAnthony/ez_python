ip_1 = "157.220.185.237"

ip_2 = "157.220.184.230"


bin_ip_1 = [bin(int(i))[2:].zfill(8) for i in ip_1.split('.')]
bin_ip_2 = [bin(int(i))[2:].zfill(8) for i in ip_2.split('.')]


# print(bin_ip_1)
# print(bin_ip_2)


left = "10011101110111001011100"
count = 0
for i in range(2**9):
    right = bin(i)[2:].zfill(9)
    if (left + right).count('1') == 15:
        count += 1


print(count)