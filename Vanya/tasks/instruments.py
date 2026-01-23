# не знаю зачем там про пустую строку сказано
# на фото не виден формат ввода, возможно иначе надо будет делать
# split() используем чтобы получить список фамилий
# (я предполагаю что фамилии идут строкой через пробел)
goboi = input().split()
fleita = input().split()
saksofon = input().split()

# список всех фамилий без дублей
all_musicians = set(goboi + fleita + saksofon)

res = []

for musician in all_musicians:
    counter = 0

    counter = (
        # логика такая же как в предыдущей задаче
        int(musician in goboi) +
        int(musician in fleita) +
        int(musician in saksofon)
    )

    if counter == 1:
        res.append(musician)

print(*res)