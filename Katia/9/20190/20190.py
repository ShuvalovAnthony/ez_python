from itertools import combinations

f = open("Katia/9/20190/20190.txt")


data = [
    [int(i) for i in row.split()] for row in f
]


def checkTriplet(triplet: tuple):
    srow = sorted(triplet)
    return srow[1]/srow[0] == srow[2]/srow[1] != 1


def check(row: list):
    for triplet in combinations(row, r=3):
        if checkTriplet(triplet):
            return True
    return False


counter = 0

for row in data:
    if check(row): counter += 1


print(counter)