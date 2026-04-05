f = open("Katia/26/85739/26.txt")


yacheyki= []
clients = []

all_summa = 0

index = 1

for row in f:
    row = [int(i) for i in row.split()]
    if len(row) == 1:
        yacheyki.append([row[0], 0, index])
        index += 1
    else:
        if row[0] <= 18*60:
            clients.append(row)
    
yacheyki = sorted(yacheyki, key=lambda x: (x[0], x[2]))
clients = sorted(clients, key=lambda x: x[0])

for client in clients:
    for i in yacheyki:
        if client[0] >= i[1]:
            all_summa += i[0]
            i[1] = client[0] + client[1]
            print(i)
            break

print(all_summa)