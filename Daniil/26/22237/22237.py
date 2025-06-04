f = open("Daniil/26/22237/26_22237.txt")

n = int(f.readline())



data = [
    [int(i) for i in row.split()] for row in f
]

avg_price = sum([i[1] for i in data])/len(data)

# id_, price, sold, total

cars = {}


for auto in data:
    id_, price, status = auto

    if price > avg_price:
        if id_ in cars:
            cars[id_][2] += 1 - status
            cars[id_][3] += 1
        else:
            cars[id_] = [id_, price, 1 - status, 1]


final_cars = []

for i in cars:
    final_cars.append(cars[i])


final_cars = sorted(final_cars, key=lambda x:(
    -x[2],
    -x[1],
    (x[3] - x[2])
))


print(final_cars[0])
print(8123*120, 145-120)