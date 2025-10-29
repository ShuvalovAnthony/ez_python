mask = "255.255.255.224"
client = "158.214.121.40"


bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]
bin_client = [bin(int(i))[2:].zfill(8) for i in client.split('.')]


print(bin_mask)
print(bin_client)

print("158.214.121.33")