f = open(r"Mihail/26/4660/26_4660.txt")
n = f.readline()


data = sorted([int(i) for i in f])
# print(len(data)) # делится на 4

# 1) - сумма всего минус каждый четвертый товар за полцены
print(sum(data) - sum(data[::4])/2)

# 2) первая четверть самых дешевых за полцены, остальное за полную цену
print(sum(data[:int(len(data)*0.25)])/2 + sum(data[int(len(data)*0.25):]))
