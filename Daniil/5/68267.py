for n in range(100, 10**5):
    str_n = str(n)

    troiki = []

    while len(str_n) >= 3:
        troiki.append(int(str_n[:3]))
        str_n = str_n[1:]

    r = max(troiki) - min(troiki)

    if r == 623:
        print(n)
        break