f = open("Matvei/9/21592/data.txt")

data = [
    [int(i) for i in row.split()] for row in f
]



def check(row: list):
    povtor = []
    unique = []

    for num in row:
        if row.count(num) == 2:
            povtor.append(num)
        elif row.count(num) == 1:
            unique.append(num)
    
    return (
        (len(povtor) == 6) and (len(unique) == 2) and
        ((max(povtor) - min(povtor))**2 > 2*(unique[0]**2 + unique[1]**2))
    )



for i in range(len(data)):
    row = data[i]

    if check(row):
        print(i + 1)


