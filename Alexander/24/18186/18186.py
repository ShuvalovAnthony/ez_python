f = open("Alexander/24/18186/24_18186.txt").read()


for i in "CDFGH":
    f = f.replace(i, "B")
f = f.replace("E", "A")


f = f.replace("BBA", " ")

print(max(len(i) for i in f.split()) + 6)