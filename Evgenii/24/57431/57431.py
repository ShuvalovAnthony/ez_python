from itertools import product

f = open("Evgenii/24/57431/1_24.txt").read()


banned = [''.join(i) for i in product("ABC", repeat=2)]


for i in banned:
    f = f.replace(i, ' ')

print(max([len(i) for i in f.split()]) + 2)