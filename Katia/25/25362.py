def delit(num):
    spisok = []
    for n in range(2, int(num**0.5)+1):
        if num%n == 0:
            # ПЕРВЫЙ ДЕЛИТЕЛЬ
            if n%100 == 11 and n!=11 and n!=num:
                spisok.append(n)
            # ВТОРОЙ ДЕЛИТЕЛЬ
            if (num//n)%100 == 11 and (num//n)!=11 and (num//n)!=num:
                spisok.append(num//n)

    # почему тут было len(spisok) < 2???? 
    if not spisok: return 0
    res = min(spisok)
    return res
                


limit = 5
for num in range(1350051, 10**10):
    if delit(num):
        print(num, delit(num))
        limit-=1
        if limit == 0:
            break