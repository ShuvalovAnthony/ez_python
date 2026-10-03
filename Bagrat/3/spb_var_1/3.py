from collections import Counter

f = open("Bagrat/3/spb_var_1/3.txt")

data = {}


for row in f:
    row = row.split()
    shop_id, sells = row[0], int(row[1])

    if shop_id not in data:
        data[shop_id] = sells
    else:
        data[shop_id] += sells


print(
    Counter(data).most_common(5)
)