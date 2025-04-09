def delitel(num):
    del_ = []
    for x in range(2, int(num**0.5)+1):
        if num%x == 0:
            del_.append(x)
            del_.append(num//x)
    # если делителей меньше 2х - возвращаем 0
    if len(del_) < 2: return 0
    # отступ!!!
    res = sorted(del_)[0] + sorted(del_)[-1]    
    return res
    

limit = 5
for i in range(452022, 10**7):
    if delitel(i) %7 == 3:
        print(i, delitel(i))
        limit -= 1
        if limit == 0:
            break