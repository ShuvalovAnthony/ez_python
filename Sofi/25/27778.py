from fnmatch import fnmatch


for num in range(271, 10**8 + 1, 271):
    if fnmatch(str(num), "12??15*6"):
        print(num, num//271)