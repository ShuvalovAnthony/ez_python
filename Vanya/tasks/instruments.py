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

all_musicians = goboi.union(fleita).union(saksofon)

res = set()

for musician in all_musicians:
    counter = 0

    counter = (
        # логика такая же как в предыдущей задаче
        int(musician in goboi) +
        int(musician in fleita) +
        int(musician in saksofon)
    )

    if counter == 1:
        res.add(musician)

for surname in res:
    print(surname)


(goboi | fleita | saksofon) - ((goboi & fleita) | (goboi & saksofon) | (fleita & saksofon))