from string import ascii_uppercase

f = open("Sofi/24/26551/24_26551.txt").read()


for letter in ascii_uppercase:
    if letter not in "ABCD":
        f = f.replace(letter, ' ')


nums = [i.lstrip("0") for i in f.split()]
nums = sorted(nums, key=lambda x: -len(x))


def getMaxEvenNum(num: str):
    while num and int(num, 14)%2 != 0:
        num = num[:-1]

    return num

max_len = 0

for num in nums:
    if not num:
        continue
    num = getMaxEvenNum(num)

    if num:
        max_len = max(max_len, len(num))


print(max_len)
