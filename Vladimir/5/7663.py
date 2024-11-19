for num in range(100, 1000):
    num1 = int(str(num)[0]) + int(str(num)[1])
    num2 = int(str(num)[1]) + int(str(num)[2])
    
    if num1 > num2:
        num3 = str(num1) + str(num2)
    else:
        num3 = str(num2) + str(num1)

    if num3 == "1412":
        print(num)  