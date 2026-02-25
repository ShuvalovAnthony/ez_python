f = open("Katia/22/24416/exmpl.txt")


data = [
    [int(i) for i in row.split()] for row in f
]

counter = 0

for sec in range(100): # для каждой секунды
    processes = 0
    # проверяем каждый процесс
    for stop, start in data: # у тебя левый столбик был стоп, поэтому так
        if start < sec <= stop: # если текущая секунда в диапазоне
            processes += 1

    if processes == 3:
        counter += 1

print(counter)