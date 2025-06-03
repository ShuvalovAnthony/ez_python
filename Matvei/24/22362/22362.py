f = open("Matvei/24/22362/24_22362.txt").read()


alph = "0123456789AB"

for i in set(f):
    if i not in alph:
        f = f.replace(i, ' ')


nums = f.split()
nums = sorted(nums, key=lambda x: len(x))


def cleanNumUntillKrat3(num: str):
    while num and (int(num, 12)%3 != 0):
        num = num[:-1]
    
    return num


approved_nums = []


for num in nums:
    num = num.lstrip("0")

    num = cleanNumUntillKrat3(num)
    if num == '': continue

    dec_num = int(num, 12)
    if dec_num%3 == 0:
        approved_nums.append([len(num), dec_num, num])


approved_nums = sorted(approved_nums, key=lambda x:(
    -x[0],
    x[1]
))

print(approved_nums[0])

print(f.index(approved_nums[0][2]))