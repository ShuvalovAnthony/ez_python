f = open("Katia/24/6636/24_6636.txt").read()


f = (f.replace("3", "1").replace("5", "1").replace("4", "2").
     replace("21", "_").replace("2", " ").replace("1", " "))


print(max([len(i) for i in f.split()]))
