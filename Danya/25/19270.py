# 1*2?3*45
def check(num: int):
    num = str(num)
    center = num[1:-2]

    flag = ""

    for i in "02468":
        if "2" + i + "3" in center:
            flag = "2" + i + "3"
    
    if not flag:
        return False
    
    center = center.replace(flag, "")

    for i in "02468":
        if i in center:
            return False


    return (
        (num[0] == "1") and
        (num[-2:] == "45") and
        flag
    )


for num in range(153, 10**8 + 1, 153):
    if check(num):
        print(num, num//153)