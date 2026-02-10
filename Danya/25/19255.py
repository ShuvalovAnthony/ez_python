from fnmatch import fnmatch


for num in range(18579, 10**10 + 1, 18579):
    if fnmatch(str(num), "54?1?3*7"):
        print(num, num//18579)