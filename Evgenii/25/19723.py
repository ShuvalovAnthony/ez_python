from fnmatch import fnmatch


for num in range(451, 10**9 + 1, 451):
    if fnmatch(str(num), "10?451*3"):
        print(num, num//451)