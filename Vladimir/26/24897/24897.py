f = open("Vladimir/26/24897/26_24897.txt")

n = int(f.readline())

doma = {}


for row in f:
    nomer_zayavki, nomer_doma, nomer_podezda = [int(i) for i in row.split()]

    if nomer_doma not in doma:
        doma[nomer_doma] = [
            [nomer_podezda, nomer_zayavki]
        ]
    else:
        doma[nomer_doma].append([nomer_podezda, nomer_zayavki])


def domProcessor(dom):
    dom = sorted(dom, key=lambda x: (x[0], x[1]))

    dom_cleaned = [dom[0]]
    max_podryad = 0
    nomer_zayvki_min_podezda = dom[0][1]
    first_podezd = dom[0][0]

    temp_max_podryad = 1
    temp_nomer_zayvki_min_podezda = dom[0][1]
    temp_first_podezd = dom[0][0]

    for zayavka in dom[1:]:
        if dom_cleaned[-1][0] == zayavka[0]:
            continue
        elif dom_cleaned[-1][0] + 1 == zayavka[0]:
            temp_max_podryad += 1
            dom_cleaned.append(zayavka)
        else:
            if temp_max_podryad > max_podryad:
                nomer_zayvki_min_podezda = temp_nomer_zayvki_min_podezda
                first_podezd = temp_first_podezd
                max_podryad = temp_max_podryad
                temp_max_podryad = 1
                
            elif temp_max_podryad == max_podryad:
                nomer_zayvki_min_podezda = min(nomer_zayvki_min_podezda, temp_nomer_zayvki_min_podezda)
                temp_max_podryad = 1
            temp_first_podezd = zayavka[0]
            dom_cleaned.append(zayavka)

    return max_podryad, nomer_zayvki_min_podezda, first_podezd


nomer_doma_answ = 0
first_podezd_answ = 0

max_podezdov = 0
min_nomer_zayvki = 10**10


for nomer_doma in doma:
    max_podryad, nomer_zayvki_min_podezda, first_podezd = domProcessor(doma[nomer_doma])

    if max_podryad > max_podezdov:
        max_podezdov = max_podryad
        first_podezd_answ = first_podezd
        min_nomer_zayvki = nomer_zayvki_min_podezda
    elif max_podryad == max_podezdov:
        if nomer_zayvki_min_podezda < min_nomer_zayvki:
            max_podezdov = max_podryad
            first_podezd_answ = first_podezd
            min_nomer_zayvki = nomer_zayvki_min_podezda


print(nomer_doma_answ, first_podezd_answ)


