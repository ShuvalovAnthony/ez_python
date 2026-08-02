def to_9(num: int):
    res = ''

    while num > 0:
        res += str(num%9)
        num //= 9

    return res[::-1]


for x in range(1, 2401):
    num = 7*9**210 + 6*9**110 - x

    num_9 = to_9(num) # str

    if num_9.count("0") == 100:
        print(x)