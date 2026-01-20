f = open(r'Katia/9/25348/25348.txt')
data = [
    [int(i) for i in row.split()] for row in f
]

def check(row:list):
    povtor = []
    uni = []
    for num in row:
        if row.count(num) == 3:
            povtor.append(num)
        if row.count(num) == 1:
            uni.append(num)

    return (len(povtor) == 3 and len(uni) == 4) and (max(row) in uni)


k = 0 
for row in data:
    if check(row):
        k += 1 
print(k)