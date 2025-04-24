f = open("Katia/9/70536/fail.txt")

data = [ 
    [int(i) for i in row.split()] for row in f
]

counter = 0 
def check(row:list):
    povtor = [] 
    nepovtor = []
    for num in row:
        if row.count(num) == 3:
            povtor.append(num)
        if row.count(num) == 1:
            nepovtor.append(num)
    if len(povtor) == 3 and len(nepovtor) == 3:
        if (sum(povtor))**2 > (sum(nepovtor))**2:
            return True

for row in data:
    if check(row):
        counter += 1
print(counter)