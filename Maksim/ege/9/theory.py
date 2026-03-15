row = [1, 2, 3, 4]

# только уникальные числа
if len(row) == len(set(row)):
    ...


#  в строке есть как повторяющиеся, так и неповторяющиеся числа;
povtor = []
uniq = []

for num in row:
    if row.count(num) == 1:
        uniq.append(num)
    else:
        povtor.append(num)