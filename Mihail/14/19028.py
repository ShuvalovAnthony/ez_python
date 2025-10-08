from itertools import product
from string import digits, ascii_uppercase


hex_alph = digits + ascii_uppercase[:6]
oct_alph = digits[:8]

hex_nums = set()
oct_nums = set()

for hex_num in product(hex_alph, repeat=6):
    hex_num = "".join(hex_num)
    if hex_num[0] != '0':
        hex_nums.add(int(hex_num[:4] + "A" + hex_num[-2:], 16))
        
for oct_num in product(oct_alph, repeat=9):
    oct_num = "".join(oct_num)
    if oct_num[0] != '0':
        oct_nums.add(int(oct_num[:4] + "2" + oct_num[-3:] + "3", 8))


common = hex_nums.intersection(oct_nums)

print(len(common))