# 564 444

f = open("Vladimir/26/23765/26_23765.txt")

sroki_hraneniya = {}
sroki_godnosti = {}

all_numbers = []

index = 1
for row in f:
    srok_hran, srok_god = [int(i) for i in row.split()]
    sroki_hraneniya[srok_hran] = index
    sroki_godnosti[srok_god] = index
    all_numbers.append(srok_god)
    all_numbers.append(srok_hran)

    index += 1


all_numbers = sorted(all_numbers)

result_left = [] # hranenie
result_right = [] # godnosti
last = -1

for num in all_numbers:
    if (num in sroki_hraneniya):
        id_ = sroki_hraneniya[num]
        if (id_ not in result_left) and (id_ not in result_right):
            result_left.append(id_)
            last = id_
    elif (num in sroki_godnosti):
        id_ = sroki_godnosti[num]
        if (id_ not in result_left) and (id_ not in result_right):
            result_right.append(id_)
            last = id_

if last in result_right:
    print(last, len(result_right) - 1)
else:
    print(last, len(result_right))
