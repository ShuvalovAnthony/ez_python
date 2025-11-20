def prost(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num%i == 0:
            return False
    return True


def delit(num):
    dell = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if (prost(i) and prost(num // i)
                    and str(num // i).count("5") == 1
                    and str(i).count("5") == 1):
                return num//i
    return 0

for num in range(1_324_727 + 1, 10**8):
    if delit(num):
        print(num, delit(num))