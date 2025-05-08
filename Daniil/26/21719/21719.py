f = open("Daniil/26/21719/26_21719.txt")

n = int(f.readline())

data = [
    [int(i) for i in row.split()] for row in f
]

data = sorted(data, key=lambda x: x[0])


data_2 = {
    # id_chet: [],
    # id_nechet: []
}


for row in data:
    id_, task = row

    if task%2 == 0:
        if (str(id_) + "even" ) in data_2:
            data_2[(str(id_) + "even" )].append(task)
        else:
            data_2[(str(id_) + "even" )] = [task]
    else:
        if (str(id_) + "odd_" ) in data_2:
            data_2[(str(id_) + "odd_" )].append(task)
        else:
            data_2[(str(id_) + "odd_" )] = [task]



def findMaxLen(tasks: list):
    tasks = sorted(set(tasks))

    max_len = 0
    temp_len = 1
    for i in range(len(tasks) - 1):
        if tasks[i + 1] - tasks[i] == 2:
            temp_len += 1
        else:
            max_len = max(max_len, temp_len)
            temp_len = 1
    
    return max_len


res = []

for id_, tasks in data_2.items():
    id_ = int(id_[:-4])
    res.append([id_, findMaxLen(tasks)])
        


res = sorted(res, key=lambda x:(
    -x[1],
    x[0]
))


print(res[0])