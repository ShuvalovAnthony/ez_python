f = open(r"Mihail/9/22546/22546.txt")

data = [[int(i) for i in row.split()] for row in f]

def check(row: list):
    sorted_row = sorted(row)
    return(
        (len(set(row)) == len(row)) and ((sorted_row[0] * sorted_row[1]) <= sum(sorted_row[2:]))
    )
count = 0
for row in data:
    if check(row):
        count += 1
print(count)

#мой ответ - 1862