f = open("Danya/22/1/1.txt")

counter = 0


for row in f:
    start, stop = [int(i) for i in row.split()]

    if (start <= 21 <= stop):
        counter += 1


print(counter)