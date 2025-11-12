def check(num):
    num = str(num)
    center = num[1:-2] # *2?3*
    is_center_ok = False

    for i in "02468":
        if f"2{i}3" in center:
            sides = center.replace(f"2{i}3", '')

            for j in "02468":
                if j in sides:
                    return False
                
            is_center_ok = True
    
    return (
        (num[0] == '1') and
        (num[-2:] == "45") and
        is_center_ok
    )


for num in range(153, 10**8 + 1, 153):
    if check(num):
        print(num, num//153)