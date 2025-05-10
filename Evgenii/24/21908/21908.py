f = open("Evgenii/24/21908/24_21908.txt").read()


alph = "0123456789ABCD"

for i in set(f):
    if i not in alph:
        f = f.replace(i, ' ')


nums = f.split()
nums = [i.lstrip("0") for i in nums]
nums = sorted(nums, key=lambda x: len(x), reverse=True)



max_len = 0


def cleanNum(num: str):
    num = num[::-1]

    while num and (num[0] in "13579BD"):
        num = num[1:]

    return num[::-1]



for num in nums:
    if num:
        max_len = max(max_len, len(cleanNum(num)))

print(max_len)

