from fnmatch import fnmatch


for i in range(7993, 10**10 + 1, 7993):
    if fnmatch(str(i), "4*4736*1"):
        print(i, i//7993)