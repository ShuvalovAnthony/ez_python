# from re import findall

# f = open(r'Katia/24/21908/24_21908.txt').read()

# pattern = r'([1-9A-D][1-9A-D]*[02468AC])'
# nums = findall(pattern, f)


# nums = sorted(nums, key=lambda x: [-len(x),int(x,14)])

# answ = nums[0]

# print(len(answ))



from string import digits, ascii_uppercase

f = open(r'Katia/24/21908/24_21908.txt').read()

alph = digits + ascii_uppercase[:4]


for symb in set(f):
    if symb not in alph:
        f = f.replace(symb, ' ')
    

nums = f.split()
nums = [i.lstrip("0") for i in nums]
nums = sorted(nums, key=lambda x: len(x), reverse=True)


def find_max_len(num):
    while num and int(num, 14)%2 != 0:
        num = num[:-1]
    return len(num)

max_len = 0

for num in nums[:10]:
    max_len = max(
        max_len,
        find_max_len(num)
    )
    

print(max_len)