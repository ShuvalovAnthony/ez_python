f = open("Katia/9/73864/73864.txt")

data = []
columns = [[] for i in range(6)]


for row in f:
    row = [int(i) for i in row.split()]
    
    data.append(row)

    for i in range(len(row)):
        columns[i].append(row[i])



def secondCond(num: int, col: int):
    return columns[col].count(num) >= 336
    

def check(row: list):
    counter = 0
    avg = sum(row)/len(row)

    for i in range(len(row)):
        num = row[i]
        if (
            # это число не встречается в других ячейках той же строки
            (row.count(num) == 1) and

            # это число встречается не менее 335 раз в других ячейках того же столбца
            secondCond(num, i) and

            # это число меньше среднего арифметического всех чисел строки
            (num < avg)
        ):
            counter += 1

    return counter == 1



counter = 0

for row in data:
    if check(row): counter += 1
print(counter)



# row 0    1   2   3   4   5
# [
#     [33, 23, 23, 59, 79, 50],
#     [70, 34, 53, 80, 83, 84],
#     [27, 99, 35, 53, 39, 98], 
#     [14, 66, 15, 72, 83, 40], 
#     [43, 6, 9, 55, 38, 10], 
#     [6, 1, 65, 54, 22, 58], 
#     [63, 84, 93, 54, 79, 98]
# ]