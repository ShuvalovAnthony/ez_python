f = open(r"Mihail/9/stat1/17.txt")

data = [int(i) for i in f]
spisok_min = []
for i in data:
    if (i < 0) and (100 <= abs(i) <= 999) and (abs(i)%6 == 0):
        spisok_min.append(i)

max_data = max(spisok_min)

def check(pari: list):
    count_minus = 0
    for i in pari:
        if i < 0:
            count_minus += 1
    return(
        (count_minus == 1) and (sum(pari) > max_data)
    )

count = 0
spisok_max = []
for i in range(len(data) - 1):
    pari = data[i:i+2]
    if check(pari):
        count += 1
        spisok_max.append(int(pari[0])**2 + int(pari[1])**2)
print(count, max(spisok_max))
#мой ответ - 2553 19701728317, файл с цифрами я скинул. правильного ответа я не нашел