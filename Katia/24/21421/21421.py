from string import ascii_uppercase

f = open("Katia/24/21421/24_21421.txt").read()


for i in ascii_uppercase[2:]:
    f = f.replace(i, ' ')


nums = f.split()
nums = sorted([num.lstrip("0") for num in nums], key=lambda x: -len(x))


for num in nums:
    if num[-1] in "02468A":
        print(len(num))
        break