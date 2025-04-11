from string import ascii_uppercase

f = open("Daniil/24/5677/24_5677.txt").read()



# f = f.replace("DAD", '_')

# for i in ascii_uppercase:
#     f = f.replace(i, ' ')

# print(max([len(i) for i in f.split()]))

#   DADDADDADDADDADDADDAD   
# AD                      DA
# D                       D

starts = ['AD', 'D', '']
endings = ['DA', 'D', '']

max_len = 0

for i in range(50, 0, -1):
    for start in starts:
        for end in endings:
            res = start + "DAD"*i + end
            if res in f:
                max_len = max(max_len, len(res))

print(max_len)