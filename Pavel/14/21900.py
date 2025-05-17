def to7(num: int):
    res = ''

    while num > 0:
        res += str(num%7)
        num //= 7

    return res[::-1]


for x in range(1, 2301):
    num = 7**350 + 7**150 - x

    sem_num = to7(num)

    if sem_num.count('0') == 200:
        print(x)
