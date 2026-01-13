spisok = []
for x in range(1, 11501):
    num = 7**270+7**170+7**70-x
    k = 0
    while num>0:
        if num%7 == 0:
            k+= 1
        num//=7
    spisok.append([x, k])

spisok = sorted(spisok, key=lambda x: (
    -x[1],
    -x[0]
))


for row in spisok:
    print(row)
    break