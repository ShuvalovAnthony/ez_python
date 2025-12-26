f = open("Katia/26/23765/26_23765.txt")

n = int(f.readline())

# срок хранения / срок годности

data = [
    [int(i) for i in row.split()] for row in f
]


# из каждой пары я добавлю в этот список - минимальное число
all_min_nums = []

for pair in data:
    all_min_nums.append(min(pair))

all_min_nums = sorted(all_min_nums)


def findPairByNum(num: int):
    for pair in data:
        if num in pair:
            return pair
        

left_rating = [] # top rating
right_rating = []


for num in all_min_nums:
    pair = findPairByNum(num)

    if pair[0] < pair[1]:
        left_rating.append(pair)
        print("left", pair)
    else:
        right_rating.append(pair)
        print("right", pair)

# 564 444

