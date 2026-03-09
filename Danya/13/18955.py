client1 = "200.154.190.12"
client2 = "200.154.184.0"

bin_client1 = [bin(int(i))[2:].zfill(8) for i in client1.split('.')]
bin_client2 = [bin(int(i))[2:].zfill(8) for i in client2.split('.')]


print(bin_client1)
print(bin_client2)

