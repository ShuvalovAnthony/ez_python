# from re import *

# # regular expressions

# f = open("Bagrat/24/17878/24_17878.txt").read()

# num = r"(0|[6789]([06789])*)"

# pattern = rf"{num}([-*]{num})*"

# nums = [i.group() for i in finditer(pattern, f)]
# lens = [len(i) for i in nums]
# print(nums)
# print(max(lens))

f = open("Bagrat/24/17878/24_17878.txt").read()

f = f.replace("-", "*")

for i in range(100, 1, -1):
    f = f.replace(i*"*", ' ')


row_nums = sorted(f.split(), key=len, reverse=True)


def check(num: str):
    num = num.lstrip("0")
    nums = num.split("*")
    max_len = 0
    temp_nums = []
    for left in range(len(nums)):
        for right in range(left + 1, len(nums)):
            temp_nums.append(nums[left: right + 1])

    for slice in temp_nums:
        flag = True
        for num in slice:
            if num[0] == "0" and len(num) > 1:
                flag = False
        if flag:
            max_len = max(max_len, len(''.join(slice)) + len(slice) - 1)

    return max_len


for row_num in row_nums[:10]:
    print(check(row_num))
    