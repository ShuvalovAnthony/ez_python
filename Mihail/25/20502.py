def check(num):
    num = str(num)
    right_part = num[6:]

    for i in "13579": 
        if i in right_part:
            return False

    return (
        (num[:2] == "20") and
        (num[2] in "13579") and
        (num[3] in "13579") and
        (num[4:6] == "22")
    )


limit = 5

for num in range(10980, 10**10 + 1, 10980):
    if check(num):
        print(num, num//10980)
        limit -= 1

    if limit == 0:
        break


