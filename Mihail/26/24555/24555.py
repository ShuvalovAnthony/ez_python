f = open("Mihail/26/24555/26_24555.txt")

n = f.readline()

data = {}

for row in f:
    ryad, mesto = [int(i) for i in row.split()]

    if ryad not in data:
        data[ryad] = [mesto]
    else:
        data[ryad].append(mesto)



res = []


def check(mesta: list):
    mesta = sorted(mesta)

    for i in range(len(mesta) - 3):
        chetverka = mesta[i: i + 4]

        flag = True
        
        for i in range(len(chetverka) - 1):
            if chetverka[i + 1] - chetverka[i] != 3:
                flag = False
                break

        if flag:
            return chetverka[0]
        
    return False



for ryad, mesta in data.items():
    if len(mesta) >= 4:
        min_mest = check(mesta)

        if min_mest:
            res.append([ryad, min_mest])



res = sorted(res, key=lambda x: (-x[0], x[1]))


for row in res[:5]:
    print(row)