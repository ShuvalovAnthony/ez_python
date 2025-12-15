f = open("Vladimir/26/25363/26_25363.txt")

n = int(f.readline())

data = [
    [int(i) for i in row.split()] for row in f
]

all_data = []

for row in data:
    all_data.append(min(row))

all_data = sorted(all_data)

rating_left = [] # от начала рейтинга
rating_right = [] # от конца


def find_pair(num):
    for row in data:
        if num in row:
            return row
        

last_number = 0
last_rating_added = ""

for num in all_data:
    pair = find_pair(num)

    if num == pair[0]:
        rating_left.append(pair)
        last_number = data.index(pair) + 1
        last_rating_added = "L"
    else:
        rating_right.append(pair)
        last_number = data.index(pair) + 1
        last_rating_added = "R"


if last_rating_added == "R":
    print(last_number, len(rating_right) - 1)
else:
    print(last_number, len(rating_right))

