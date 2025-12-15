mask = "255.255.252.0"
client = "190.202.83.62"


bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_client = [bin(int(i))[2:].zfill(8) for i in client.split(".")]


print(bin_mask)
print(bin_client)

['10111110', '11001010', '010100  11', '00111110']
['11111111', '11111111', '111111  00', '00000000']


print(['10111110', '11001010', '01010011', '11111110'])