def check(num: int):
    num = str(num)

    left = num[:-5]
    if any([i for i in left if i in '13579']):
        return False

    return (
        (num[-1] in '13579') and
        (num[-2] == '4') and 
        (num[-3] in '13579') and
        (num[-4] == '2') and
        (num[-5] == '1')
    )



for num in range(9231, 10**10 + 1, 9231):
    if check(num):
        print(num, num//9231)