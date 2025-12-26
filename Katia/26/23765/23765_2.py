f = open("Katia/26/23765/26_23765.txt")

n = int(f.readline())

# срок хранения / срок годности

data = [
    [int(i) for i in row.split()] for row in f
]

data = sorted(data, key=lambda pair: min(pair))

left_rating = [] # top rating
right_rating = []


for pair in data:

    if pair[0] < pair[1]:
        left_rating.append(pair)
        print("left", pair)
    else:
        right_rating.append(pair)
        print("right", pair)

# 564 444
print(len(right_rating) - 1)