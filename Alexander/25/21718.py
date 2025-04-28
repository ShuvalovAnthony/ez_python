from fnmatch import fnmatch


for num in range(7993, 10**10, 7993):
    if fnmatch(str(num), "4*4736*1"):
        print(num, num//7993)