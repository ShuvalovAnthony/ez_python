from math import ceil, floor

for info_byte in range(10_000):
    id = 4*5 # bit
    struct = 70*11 # bit
    id_and_struct_byte = ceil((id + struct)/8)
    obj = id_and_struct_byte + info_byte

    if obj*131_072 == 24*1024*1024:
        print(info_byte)
