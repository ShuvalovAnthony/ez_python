def pr(num):
    p = 1
    while num>0:
        n = num%10
        p = p*n
        num //= 10
    return p 

print(pr(123))


from fnmatch import fnmatch


for num in range(4321, 10**9, 4321):
    if fnmatch(str(num), '34*56?7') and str(pr(num))[-1] == '0':
        print(num, num//4321)