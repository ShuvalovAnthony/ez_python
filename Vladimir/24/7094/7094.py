f = open("Vladimir/24/7094/24_7094.txt").read()

# A, C, D, F и U

f = f.replace("U", "A").replace("F", "C").replace("D", "C")


for i in range(10**6):
    if "CA"*i in f:
        print(i)
    else:
        break