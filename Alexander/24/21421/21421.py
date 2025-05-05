f = open("Alexander/24/21421/24_21421.txt").read()

alph = "0123456789AB"

for letter in set(f):
    if letter not in alph:
        f = f.replace(letter, " ")


nums = [i.lstrip("0") for i in f.split()]


chetnie = []

for num in set(nums):
    if num and (num[-1] in "02468A"):
        chetnie.append(num)



print(max(len(i) for i in chetnie))
