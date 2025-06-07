f = open("Polina/9/21895/data.txt")


data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list): # row = [5, 7, 19, 0, 4]
    if len(set(row)) < 5: return False

    row = sorted(row)
    # [0, 4, 5, 7, 19]
    # return sum(row[-2:]) <= sum(row[:3])
    return row[-1] + row[-2] <= row[0] + row[1] + row[2]


counter = 0

for row in data:
    if check(row):
        counter += 1

print(counter)
