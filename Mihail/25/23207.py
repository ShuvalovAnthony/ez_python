# def prost(num):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num%i == 0:
#             return False
#     return True


# def delit(num):
#     dell = []
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             if (prost(i) and prost(num // i)
#                     and str(num // i).count("5") == 1
#                     and str(i).count("5") == 1):
#                 return num//i
#     return 0

# for num in range(1_324_727 + 1, 10**8):
#     if delit(num):
#         print(num, delit(num))


def prost(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def delit(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: # НАШЛИ ПАРУ ДЕЛИТЕЛЕЙ
            first = i
            second = num//i
            if (
                (str(first).count("5") == 1) and
                (str(second).count("5") == 1) and
                prost(first) and prost(second)
            ):
                return second
                
    return False

k = 0
for i in range(1324727 + 1, 10**100):
    if delit(i):
        print(i, delit(i))
        k += 1
    
    if k == 5:
        break
            
            