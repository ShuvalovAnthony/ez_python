from string import digits, ascii_uppercase


f = open("Mihail/24/26551/24_26551.txt").read()

alph = digits + ascii_uppercase[:4]


for digit in set(f):
    if digit not in alph:
        f = f.replace(digit, ' ')


nums = f.split()
nums = [i.lstrip("0") for i in nums]
nums = sorted(nums, key=lambda x: len(x), reverse=True)

def find_len_chet(num: str):
    while num and int(num, 14)%2 != 0:
        num = num[:-1]
    return len(num)



max_len = 0

for num in nums[:100]:
    max_len = max(max_len, find_len_chet(num))


print(max_len)