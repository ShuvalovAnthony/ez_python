def chet(num):
    s =""
    while num > 0:
        s += str(num%4)
        num //= 4
    return s[::-1]

min_r = 1000000
max_num = 0

for num in range(1,100000):
    chet_num = chet(num)
    sum_cifr = sum([int(i) for i in str(chet_num)])
    if sum_cifr %3 == 0:
        chet_num = chet_num.replace('0', '*')
        chet_num = chet_num.replace('2', '0')
        chet_num = chet_num.replace('*', '2')
        chet_num = "32" + chet_num
    else:
        chet_num += "33"
        chet_num = chet_num[0] + "10" + chet_num[3:]

    r = int(chet_num, 4)

    if r > 320:
        if r <= min_r:
            min_r = r
            max_num = num

print(max_num)

