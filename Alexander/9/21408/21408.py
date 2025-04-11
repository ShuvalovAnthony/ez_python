f = open("Alexander/9/21408/data.txt")


data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    povtor = []
    unique = []

    for num in row:
        if row.count(num) == 3:
            povtor.append(num)
        elif row.count(num) == 1:
            unique.append(num)
        else:
            return False
        
    if len(unique) != 1: return False
    if len(povtor) != 6: return False

    return max(povtor) > unique[0]

count = 0


for row in data:
    count += check(row)

print(count)