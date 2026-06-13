f = open("Mihail/24/16269 /24_16269.txt").readline()


for i in 'TUVW':
   f = f.replace(i, ' ')

for i in 'XYZ':
    while i*4 in f:
        f = f.replace(i*4, i*2 + ' ' + i*2)
    while i*3 in f:
        f = f.replace(i*3, i*2 + ' ' + i*2)
    f = f.replace(i*2, '*').replace(i, ' ')

print(max(map(len, f.split()))*2)
