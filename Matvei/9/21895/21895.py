f = open("Matvei/9/21895/data.txt")


data = [
    [int(i) for i in row.split()] for row in f
]



def check(row: list):
    row = sorted(row)
    # [1, 1, 3, 4, 5]

    return (
        (len(set(row)) == 5) and
        (sum(row[-2:]) <= sum(row[:3]))
    )



counter = 0

for row in data:
    if check(row):
        counter += 1

print(counter)