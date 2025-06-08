def six(x):
    s = ''
    while x != 0:
        s = str(x%6)+s
        x = x//6
    return s


min_r = 10**6
max_n = 0


for n in range(1,5000):
    z = six(n)
    if (z.count('1')*1 +z.count('2')*2 +
        z.count('3')*3 +z.count('4')*4 +
        z.count('5')*5) % 5 == 0:
        z = z.replace('0','*').replace('3','0').replace('*','3')
        z = '11'+z

    else:
        z = z +'44'
        z = z[0] + '05' + z[3:]

    r = int(z,6)
    if r > 1500:
        if r < min_r:
            min_r = r
            max_n = n
        elif r == min_r:
            max_n = max(max_n, n)

print(max_n)