f = open(r"Mihail/17/2403/17_2403.txt")
data = [int(i) for i in f]


def check(pari: list):
    first, second = pari
    return (
        (first%9 == 0 and oct(second)[-1] == "3" and second%9 != 0) or
        (second%9 == 0 and oct(first)[-1] == "3" and first%9 != 0)
    )


spisok = []
k = 0

for i in range(len(data) - 1):
    pari = data[i:i+2]
    if check(pari):
        k += 1
        spisok.append(max(pari))
print(k, max(spisok))