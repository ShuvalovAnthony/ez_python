def check(num: str):
    # 1  *2?3*  45
    middle_part = num[1:-2]
    usl = False
    for i in "02468":
        s = ("2" + i + "3")
        if s in middle_part:
            splitted = middle_part.split(s)
            splitted = splitted[0] + splitted[1]
            for j in "02468":
                if j in splitted:
                    return False
            usl = True

    return (
        (num[0] == "1") and
        (num[-2:] == "45") and
        usl
    )



for num in range(153, 10**8 + 1, 153):
    if check(str(num)):
        print(num, num//153)