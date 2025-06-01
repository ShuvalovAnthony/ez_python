f = open("Polina/24/952/24_952.txt").read()


f = f.replace("E", "A").split("A")


print(max([len(i) for i in f]))