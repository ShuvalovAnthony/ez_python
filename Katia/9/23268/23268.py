f = open(r'Katia/9/23268/23268.txt')
index = 0



data = [
    [int(i) for i in row.split()] for row in f
]


def check(row:list):
    uni = []
    povtor = []
    for num in row:
        if row.count(num) == 2:
            povtor.append(num)
        
        elif row.count(num) == 1:
            uni.append(num)
    return (
        ((len(povtor)== 4) and (len(uni )== 3)) and
        ((sum(povtor))/4 < max(uni))
    )

    
for row in data:
    index += 1
    if check(row):
        print(index)
        break