f = open("Polina/24/22362/24_22362.txt").read()


alph = "0123456789AB"

for i in set(f):
    if i not in alph:
        f = f.replace(i, " ")


nums = f.split()
nums = sorted(nums, key=lambda x:len(x), reverse=True)


max_len = 0
first_symb_index = 0
res_num = "1"*1000


def cutUntilKrat3(num: str):
    while (len(num) > 1) and (int(num, 12)%3 != 0):
        num = num[-1]

        if len(num) < max_len:
            return ''
    return num



for num in nums:

    num = num.lstrip("0")
    num = cutUntilKrat3(num)

    if num == '': continue

    if (len(num) > max_len):
        max_len = len(num)
        first_symb_index = f.index(num)
        res_num = num
    elif len(num) == max_len:
        if int(num, 12) < int(res_num, 12):
            res_num = num
            first_symb_index = f.index(num)


print(first_symb_index, max_len)


