def chetver(n: int):
    res = ''

    while n > 0:
        res += str(n%4)
        n //= 4

    return res[::-1]


max_zeros = 0
min_x = None


for x in range(1, 3001):
    num = 4**210 + 4**110 - x

    num_chet = chetver(num)

    if num_chet.count('0') > max_zeros:
        max_zeros = num_chet.count('0')
        min_x = x


print(min_x)