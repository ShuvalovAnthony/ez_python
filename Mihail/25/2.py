def prost(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def delit(num):
    init_num = num
    delitetli = set()
    
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            if prost(i) and str(i).count('1') == 1:
                delitetli.add(i)
            if prost(num//i) and str(num//i).count('1') == 1:
                delitetli.add(num//i)

    razlozhenie = []

    for delitel in delitetli:
        while num%delitel == 0:
            razlozhenie.append(delitel)
            num //= delitel

    proizv = 1
    for delitel in razlozhenie:
        proizv *= delitel

    if len(razlozhenie) == 3 and proizv == init_num:
        return razlozhenie 
    
    return []

k = 0
for i in range(15_381_264 + 1, 10**100):
    if len(delit(i)) == 3:
        print(i, max(delit(i)))
        k += 1
    if k == 5:
        break
