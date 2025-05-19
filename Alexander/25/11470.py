nums = []


for dv in range(40):
    for tri in range(30):
        for pyat in range(20):
            num = 2**dv*3**tri*5**pyat

            if 10**10 <= num <= 10**11:
                nums.append(num)


print(sorted(nums)[-5:])