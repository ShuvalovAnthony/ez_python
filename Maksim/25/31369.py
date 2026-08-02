def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False

    return True


def isSixSeven(num):
    return str(num).count("67") == 1


def check(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            # i, num//i - множители
            if (
                (isPrime(i) and isSixSeven(i)) and
                (isPrime(num//i) and isSixSeven(num//i))
            ):
                return i

    return 0


limit = 5


for num in range(2_726_695_892, 10**10):
    res = check(num)
    if res:
        print(num, res)
        limit -= 1

    if limit == 0:
        break