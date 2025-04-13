f = open("Evgenii/9/73864/data.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    avg = sum(row)/len(row)
    numbers_to_check = []

    for i in range(len(row)):
        if (row.count(row[i]) == 1) and (row[i] < avg):
            numbers_to_check.append(row[i])
        else:
            numbers_to_check.append(0)
    if not any(numbers_to_check): return False
    interesting_numbers = 0
    for i in range(len(row)):
        if numbers_to_check[i] == 0: continue
        usl2 = False

        repeat_counter = 0
        for row_ in data:
            if row[i] == row_[i]:
                repeat_counter += 1
        if repeat_counter >= 336:
            usl2 = True

        if usl2:
            interesting_numbers += 1
    return interesting_numbers == 1
    

counter = 0


for i in range(len(data)):
    if check(data[i]):
        counter += 1
    
    if i%1000 == 0:
        print(i)

print(counter)