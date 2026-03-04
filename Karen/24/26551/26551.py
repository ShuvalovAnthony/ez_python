from string import digits, ascii_uppercase

f = open("Karen/24/26551/24_26551.txt").read()

alph = digits + ascii_uppercase[:4]


for i in ascii_uppercase:
    if i not in alph:
        f = f.replace(i, ' ')


nums = f.split()
nums = [i.lstrip("0") for i in nums]
nums = sorted(nums, key=lambda x: -len(x))

max_len = 0


def getShortestEvenNum(s: str):
    while s and int(s, 14)%2 != 0:
        s = s[:-1]
    return s


for num in nums[:10]:
    num = getShortestEvenNum(num)
    max_len = max(max_len, len(num))


print(max_len)