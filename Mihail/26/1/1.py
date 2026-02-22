f = open("Mihail/26/1/26.txt")

n = f.readline()

data = {}


for row_ in f:
    row, place = [int(i) for i in row_.split()]

    if row not in data:
        data[row] = [place]
    else:
        data[row].append(place)



def check(places: list):
    places = sorted(places)

    for i in range(len(places) - 1):
        left = places[i]
        right = places[i + 1]

        if right - left == 12:
            return left + 1
    return False


min_row = 10**10
min_place = 10**10


for row, places in data.items():
    if len(places) < 2:
        continue

    res = check(places)

    if res:
        if row < min_row:
            min_row = row
            min_place = res


print(min_row, min_place)