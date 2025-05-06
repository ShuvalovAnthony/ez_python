f = open('Alexander/24/21908/24_21908.txt').read()

alph = '0123456789ABCD'

for letter in set(f):
    if letter not in alph:
        f = f.replace(letter,' ')

nums = [i.lstrip('0') for i in f.split()]


maxx = []

for num in set(nums):
    if not num: continue

    if num[-1] in "02468AC":
        maxx.append(len(num))
    else:
        while num and (num[-1] not in "02468AC"):
            num = num[:-1]
        
        if num:
            maxx.append(len(num))


print(max(maxx))

        
    