goboi = set()
while True:
    surname = input()
    if surname == "":
        break
    goboi.add(surname)

fleita = set()
while True:
    surname = input()
    if surname == "":
        break
    fleita.add(surname)

saksofon = set()
while True:
    surname = input()
    if surname == "":
        break
    saksofon.add(surname)

res = goboi.union(fleita, saksofon)

for surname in goboi^fleita^saksofon:
    print(surname)