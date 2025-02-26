def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0: return False
    return True


for twos in range(41, 100):
    a = "0" + "1"*40 + "2"*twos + "0"

    while "00" not in a:
        a = a.replace("02", "101", 1)
        a = a.replace("11", "2", 1)
        a = a.replace("012", "30", 1)
        a = a.replace("010", "00", 1)

    summa_cifr = sum([int(i) for i in a])

    if isPrime(summa_cifr):
        print(twos)