# net
mask = "255.192.0.0"
client = "191.128.66.83"


bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]
bin_client = [bin(int(i))[2:].zfill(8) for i in client.split('.')]


print(bin_mask)
print(bin_client)


['11111111', '11    000000', '00000000', '00000000']
['10111111', '10    000000', '01000010', '01010011']




answ = ['10111111', '10111111', '11111111', '11111110']

print([int(i, 2) for i in answ])


191191255254