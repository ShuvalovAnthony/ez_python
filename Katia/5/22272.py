def dev(n):
    s = ""
    while n > 0:
        s += str(n%9)
        n//=9
    return s[::-1]


for n in range(1,1000):
    dev_num = dev(n)
    if dev_num[0] == "7":
        dev_num = dev_num.replace("3", "*")
        dev_num = dev_num.replace("6", "3")
        dev_num = dev_num.replace("*", "6")
        dev_num = "34" + dev_num
    else:
        dev_num += "45" 
        dev_num = "3" + dev_num[1:]

    r = int(dev_num, 9)

    if r < 2876:
        print(n)




def check(num: str):
    for i in "0123456789": # сюда пишешь все символы, которые нельзя подряд писать - любой набор
        num = num.replace(i, "_")

    return "__" in num
