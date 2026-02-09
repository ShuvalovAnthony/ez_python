f = open(r'Katia/24/25361/24_25361.txt').read()

for i in "2468":
    f = f.replace(i, "0")


indexes = []

for i in range(len(f)):
    if f[i] == 'F':
        indexes.append(i)


def find_max_poss_len(substr: str):
    left_f_index = substr.index("F")
    for i in range(left_f_index, len(substr)):
        if substr[i] == "0":
            return 0

    left_part_before_first_f = substr[:left_f_index]
    if "0" not in left_part_before_first_f:
        return 0
    
    left_part_valid_len = 0
    for i in range(len(left_part_before_first_f) - 1, -1, -1):
        if left_part_before_first_f[i] != '0':
            left_part_valid_len += 1
        else:
            return left_part_valid_len + 1 + len(substr) - substr.index("F")


max_len = 0 

for i in range(len(indexes)-77):
    left = indexes[i]
    right = indexes[i+77]
    substr = f[left + 1:right]
    
    # print(substr.count("F"), substr[:5], substr[-5:])
    
    if substr.count("F") == 76:
        max_len = max(max_len, find_max_poss_len(substr))

    

print(max_len)