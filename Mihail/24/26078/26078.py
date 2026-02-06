f = open(r"Mihail/24/26078/24_26078.txt").read()
indexes = []

for i in range(len(f)):
    if f[i] == "W":
        indexes.append(i)

spisok =[]

for i in range(len(indexes) - 89):
    left = indexes[i]
    right = indexes[i + 89]
    substring = f[left:right + 1]
    
    if substring.count('2025') >= 110:
        spisok.append([substring.count('W'), substring.count('2025'), len(substring)])

spisok = sorted(spisok, key=lambda x: (
    x[2],
    x[1]
    )
)


for i in spisok[:10]:
    print(i)