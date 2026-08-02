from fnmatch import fnmatch


for num in range(171, 10**8 + 1, 171):
    if fnmatch(str(num), "1*23??56"):
        print(num, num//171)