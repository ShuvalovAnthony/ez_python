k = 0 # тут храним НОМЕР СТРОКИ

for s in open("Karen/9/23268/23268.txt"):
    a = [int(x) for x in s.split()]
    
    k += 1

    a2 = [x for x in a if a.count(x)==2]
    a1 = [x for x in a if a.count(x)==1]
    
    # две пары         и 3 уникальных    сред ариф меньше макс уникального
    if len(a2) == 4 and len(a1) == 3 and sum(a2)/4 < max(a1):
        print(k)
        break


f = open("Karen/9/23268/23268.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    povtor = []
    uniq = []

    for num in row:
        if row.count(num) == 2:
            povtor.append(num)
        if row.count(num) == 1:
            uniq.append(num)

    return (
        # 1ое условие
        (len(povtor) == 4 and len(uniq) == 3) and
        # 2ое условие
        (sum(povtor)/len(povtor) < max(uniq))
    )



for i in range(len(data)):
    row = data[i]

    if check(row):
        print(i + 1) # +1 так как люди начинают отсчет с 1, а комп с 0
        break


