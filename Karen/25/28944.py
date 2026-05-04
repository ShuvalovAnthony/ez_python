def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True


def getDeliteli(num):
    deliteli = []

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            # i - первый делитель 
            # num//i - второй делитель
            if isPrime(i) and str(i).count("3") == 2:
                deliteli.append(i)

            if isPrime(num//i) and str(num//i).count("3") == 2:
                deliteli.append(num//i)

    if (
        (len(deliteli) == 2) and
        (deliteli[0]*deliteli[1] == num)
        ):
        return max(deliteli)
    
    return False


limit = 5

for num in range(8_996_453, 10**10):
    f = getDeliteli(num) # 133

    if f:
        print(num, f)
        limit -= 1

    if limit == 0:
        break
    